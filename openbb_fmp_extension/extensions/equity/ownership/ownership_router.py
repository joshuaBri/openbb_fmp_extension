"""Ownership Router."""
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

router = Router(prefix="/ownership")

@router.command(
    model="Form13FHR",
    examples=[
        APIEx(
            parameters={
                "symbol": "0001388838",
                "date": "2021-09-30",
                "provider": "fmp",
            }
        ),
    ],
)
async def form_13f(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the income statement for a given company."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="GovernmentTrades",
    examples=[
        APIEx(
            parameters={
                "chamber": "all",
                "symbol": "AAPL",
                "limit": 500,
                "provider": "fmp",
            }
        ),
        APIEx(
            parameters={
                "chamber": "all",
                "limit": 300,
                "provider": "fmp",
            }
        ),
    ],
)
async def government_trades(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the income statement for a given company."""
    return await OBBject.from_query(Query(**locals()))



"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetPortfolioSummaryRequest``."""

from typing_extensions import TypedDict


class GetPortfolioSummaryRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetPortfolioSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPortfolioSummaryRequest:
    out: GetPortfolioSummaryRequest = {}  # type: ignore[typeddict-item]
    return out

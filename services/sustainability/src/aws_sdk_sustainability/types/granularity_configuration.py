"""Generated from Smithy shape ``com.amazonaws.sustainability#GranularityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.month


class GranularityConfiguration(TypedDict):
    fiscal_year_start_month: "aws_sdk_sustainability.types.month.Month"
    """<p> The month (1-12) when the fiscal year begins. Used for <code>YEARLY_FISCAL</code> and <code>QUARTERLY_FISCAL</code> granularity. Defaults to 1 (January). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GranularityConfiguration) -> dict:
    out: dict = {}
    out["FiscalYearStartMonth"] = value.get("fiscal_year_start_month", 1)
    return out


def deserialize_json(data: dict) -> GranularityConfiguration:
    out: GranularityConfiguration = {}  # type: ignore[typeddict-item]
    if "FiscalYearStartMonth" in data:
        out["fiscal_year_start_month"] = data["FiscalYearStartMonth"]
    else:
        out["fiscal_year_start_month"] = 1
    return out

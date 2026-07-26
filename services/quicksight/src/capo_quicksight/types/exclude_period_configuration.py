"""Generated from Smithy shape ``com.amazonaws.quicksight#ExcludePeriodConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.integer
    import capo_quicksight.types.time_granularity
    import capo_quicksight.types.widget_status


class ExcludePeriodConfiguration(TypedDict, closed=True):
    amount: "capo_quicksight.types.integer.Integer"
    """<p>The amount or number of the exclude period.</p>"""
    granularity: "capo_quicksight.types.time_granularity.TimeGranularity"
    """<p>The granularity or unit (day, month, year) of the exclude period.</p>"""
    status: NotRequired["capo_quicksight.types.widget_status.WidgetStatus"]
    """<p>The status of the exclude period. Choose from the following options:</p> <ul> <li> <p> <code>ENABLED</code> </p> </li> <li> <p> <code>DISABLED</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExcludePeriodConfiguration) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    import capo_quicksight.types.time_granularity

    out["Granularity"] = capo_quicksight.types.time_granularity.serialize_json(
        value["granularity"]
    )
    if "status" in value:
        import capo_quicksight.types.widget_status

        out["Status"] = capo_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ExcludePeriodConfiguration:
    out: ExcludePeriodConfiguration = {}  # type: ignore[typeddict-item]
    if "Amount" in data:
        out["amount"] = data["Amount"]
    else:
        raise DeserializationError("ExcludePeriodConfiguration.amount required")
    if "Granularity" in data:
        import capo_quicksight.types.time_granularity

        out["granularity"] = capo_quicksight.types.time_granularity.deserialize_json(
            data["Granularity"]
        )
    else:
        raise DeserializationError("ExcludePeriodConfiguration.granularity required")
    if "Status" in data:
        import capo_quicksight.types.widget_status

        out["status"] = capo_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    return out

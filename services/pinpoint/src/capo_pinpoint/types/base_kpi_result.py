"""Generated from Smithy shape ``com.amazonaws.pinpoint#BaseKpiResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.list_of_result_row


class BaseKpiResult(TypedDict, closed=True):
    rows: NotRequired["capo_pinpoint.types.list_of_result_row.ListOfResultRow"]
    """<p>An array of objects that provides the results of a query that retrieved the data for a standard metric that applies to an application, campaign, or journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaseKpiResult) -> dict:
    out: dict = {}
    if "rows" in value:
        import capo_pinpoint.types.list_of_result_row

        out["Rows"] = capo_pinpoint.types.list_of_result_row.serialize_json(
            value["rows"]
        )
    return out


def deserialize_json(data: dict) -> BaseKpiResult:
    out: BaseKpiResult = {}  # type: ignore[typeddict-item]
    if "Rows" in data:
        import capo_pinpoint.types.list_of_result_row

        out["rows"] = capo_pinpoint.types.list_of_result_row.deserialize_json(
            data["Rows"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.pinpoint#ResultRow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.list_of_result_row_value


class ResultRow(TypedDict, closed=True):
    grouped_bys: NotRequired[
        "capo_pinpoint.types.list_of_result_row_value.ListOfResultRowValue"
    ]
    """<p>An array of objects that defines the field and field values that were used to group data in a result set that contains multiple results. This value is null if the data in a result set isn’t grouped.</p>"""
    values: NotRequired[
        "capo_pinpoint.types.list_of_result_row_value.ListOfResultRowValue"
    ]
    """<p>An array of objects that provides pre-aggregated values for a standard metric that applies to an application, campaign, or journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultRow) -> dict:
    out: dict = {}
    if "grouped_bys" in value:
        import capo_pinpoint.types.list_of_result_row_value

        out["GroupedBys"] = capo_pinpoint.types.list_of_result_row_value.serialize_json(
            value["grouped_bys"]
        )
    if "values" in value:
        import capo_pinpoint.types.list_of_result_row_value

        out["Values"] = capo_pinpoint.types.list_of_result_row_value.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> ResultRow:
    out: ResultRow = {}  # type: ignore[typeddict-item]
    if "GroupedBys" in data:
        import capo_pinpoint.types.list_of_result_row_value

        out["grouped_bys"] = (
            capo_pinpoint.types.list_of_result_row_value.deserialize_json(
                data["GroupedBys"]
            )
        )
    if "Values" in data:
        import capo_pinpoint.types.list_of_result_row_value

        out["values"] = capo_pinpoint.types.list_of_result_row_value.deserialize_json(
            data["Values"]
        )
    return out

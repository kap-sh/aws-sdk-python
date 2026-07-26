"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringListFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_string_filter_static_value_list


class DataSetStringListFilterValue(TypedDict, closed=True):
    static_values: NotRequired[
        "capo_quicksight.types.data_set_string_filter_static_value_list.DataSetStringFilterStaticValueList"
    ]
    """<p>A list of static string values used for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringListFilterValue) -> dict:
    out: dict = {}
    if "static_values" in value:
        import capo_quicksight.types.data_set_string_filter_static_value_list

        out["StaticValues"] = (
            capo_quicksight.types.data_set_string_filter_static_value_list.serialize_json(
                value["static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetStringListFilterValue:
    out: DataSetStringListFilterValue = {}  # type: ignore[typeddict-item]
    if "StaticValues" in data:
        import capo_quicksight.types.data_set_string_filter_static_value_list

        out["static_values"] = (
            capo_quicksight.types.data_set_string_filter_static_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    return out

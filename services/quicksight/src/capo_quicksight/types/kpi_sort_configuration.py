"""Generated from Smithy shape ``com.amazonaws.quicksight#KPISortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options_list


class KPISortConfiguration(TypedDict, closed=True):
    trend_group_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the trend group fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPISortConfiguration) -> dict:
    out: dict = {}
    if "trend_group_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["TrendGroupSort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["trend_group_sort"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPISortConfiguration:
    out: KPISortConfiguration = {}  # type: ignore[typeddict-item]
    if "TrendGroupSort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["trend_group_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["TrendGroupSort"]
            )
        )
    return out

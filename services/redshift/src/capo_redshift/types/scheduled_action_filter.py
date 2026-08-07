"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.scheduled_action_filter_name
    import capo_redshift.types.value_string_list


class ScheduledActionFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_redshift.types.scheduled_action_filter_name.ScheduledActionFilterName"
    ]
    """<p>The type of element to filter. </p>"""
    values: NotRequired["capo_redshift.types.value_string_list.ValueStringList"]
    """<p>List of values. Compare if the value (of type defined by <code>Name</code>) equals an item in the list of scheduled actions. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        import capo_redshift.types.scheduled_action_filter_name

        capo_redshift.types.scheduled_action_filter_name.serialize_query(
            value["name"], pairs, f"{key_prefix}Name"
        )
    if "values" in value:
        import capo_redshift.types.value_string_list

        capo_redshift.types.value_string_list.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_query(el: Element) -> ScheduledActionFilter:
    out: ScheduledActionFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        import capo_redshift.types.scheduled_action_filter_name

        out["name"] = (
            capo_redshift.types.scheduled_action_filter_name.deserialize_query(
                child_name
            )
        )
    child_values = el.find("Values")
    if child_values is not None:
        import capo_redshift.types.value_string_list

        out["values"] = capo_redshift.types.value_string_list.deserialize_query(
            child_values
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_instance_filter_name
    import capo_cloudformation.types.stack_instance_filter_values


class StackInstanceFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_cloudformation.types.stack_instance_filter_name.StackInstanceFilterName"
    ]
    """<p>The type of filter to apply.</p>"""
    values: NotRequired[
        "capo_cloudformation.types.stack_instance_filter_values.StackInstanceFilterValues"
    ]
    """<p>The status to filter by.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        import capo_cloudformation.types.stack_instance_filter_name

        capo_cloudformation.types.stack_instance_filter_name.serialize_query(
            value["name"], pairs, f"{key_prefix}Name"
        )
    if "values" in value:
        pairs.append((f"{key_prefix}Values", str(value["values"])))


def deserialize_query(el: Element) -> StackInstanceFilter:
    out: StackInstanceFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        import capo_cloudformation.types.stack_instance_filter_name

        out["name"] = (
            capo_cloudformation.types.stack_instance_filter_name.deserialize_query(
                child_name
            )
        )
    child_values = el.find("Values")
    if child_values is not None:
        out["values"] = str(child_values.text or "")
    return out

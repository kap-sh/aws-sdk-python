"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_instance_filter_name
    import aws_sdk_cloudformation.types.stack_instance_filter_values


class StackInstanceFilter(TypedDict):
    name: NotRequired[
        "aws_sdk_cloudformation.types.stack_instance_filter_name.StackInstanceFilterName"
    ]
    """<p>The type of filter to apply.</p>"""
    values: NotRequired[
        "aws_sdk_cloudformation.types.stack_instance_filter_values.StackInstanceFilterValues"
    ]
    """<p>The status to filter by.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        import aws_sdk_cloudformation.types.stack_instance_filter_name

        aws_sdk_cloudformation.types.stack_instance_filter_name.serialize_query(
            value["name"], pairs, f"{prefix}.Name"
        )
    if "values" in value:
        pairs.append((f"{prefix}.Values", str(value["values"])))


def deserialize_query(el: Element) -> StackInstanceFilter:
    out: StackInstanceFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        import aws_sdk_cloudformation.types.stack_instance_filter_name

        out["name"] = (
            aws_sdk_cloudformation.types.stack_instance_filter_name.deserialize_query(
                child_name
            )
        )
    child_values = el.find("Values")
    if child_values is not None:
        out["values"] = str(child_values.text or "")
    return out

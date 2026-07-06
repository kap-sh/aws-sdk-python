"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationResultFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.operation_result_filter_name
    import aws_sdk_cloudformation.types.operation_result_filter_values


class OperationResultFilter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_cloudformation.types.operation_result_filter_name.OperationResultFilterName"
    ]
    """<p>The type of filter to apply.</p>"""
    values: NotRequired[
        "aws_sdk_cloudformation.types.operation_result_filter_values.OperationResultFilterValues"
    ]
    """<p>The value to filter by.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationResultFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        import aws_sdk_cloudformation.types.operation_result_filter_name

        aws_sdk_cloudformation.types.operation_result_filter_name.serialize_query(
            value["name"], pairs, f"{prefix}.Name"
        )
    if "values" in value:
        pairs.append((f"{prefix}.Values", str(value["values"])))


def deserialize_query(el: Element) -> OperationResultFilter:
    out: OperationResultFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        import aws_sdk_cloudformation.types.operation_result_filter_name

        out["name"] = (
            aws_sdk_cloudformation.types.operation_result_filter_name.deserialize_query(
                child_name
            )
        )
    child_values = el.find("Values")
    if child_values is not None:
        out["values"] = str(child_values.text or "")
    return out

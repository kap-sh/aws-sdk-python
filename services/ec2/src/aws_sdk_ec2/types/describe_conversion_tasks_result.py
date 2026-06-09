"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTasksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_conversion_task_list


class DescribeConversionTasksResult(TypedDict):
    conversion_tasks: NotRequired[
        "aws_sdk_ec2.types.describe_conversion_task_list.DescribeConversionTaskList"
    ]
    """<p>Information about the conversion tasks.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeConversionTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "conversion_tasks" in value:
        import aws_sdk_ec2.types.describe_conversion_task_list

        aws_sdk_ec2.types.describe_conversion_task_list.serialize_ec2_query(
            value["conversion_tasks"], pairs, f"{prefix}.ConversionTasks"
        )


def deserialize_ec2_query(el: Element) -> DescribeConversionTasksResult:
    out: DescribeConversionTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("ConversionTasks") is not None:
        import aws_sdk_ec2.types.describe_conversion_task_list

        out["conversion_tasks"] = (
            aws_sdk_ec2.types.describe_conversion_task_list.deserialize_ec2_query(
                el, "ConversionTasks"
            )
        )
    return out

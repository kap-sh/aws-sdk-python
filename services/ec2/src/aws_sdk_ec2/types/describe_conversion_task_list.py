"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task

DescribeConversionTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.conversion_task.ConversionTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeConversionTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.conversion_task

        aws_sdk_ec2.types.conversion_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> DescribeConversionTaskList:
    import aws_sdk_ec2.types.conversion_task

    out: DescribeConversionTaskList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.conversion_task.deserialize_ec2_query(child))
    return out

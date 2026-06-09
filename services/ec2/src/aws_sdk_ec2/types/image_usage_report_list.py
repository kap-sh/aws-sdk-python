"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReportList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_report

ImageUsageReportList: TypeAlias = list[
    "aws_sdk_ec2.types.image_usage_report.ImageUsageReport"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageReportList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.image_usage_report

        aws_sdk_ec2.types.image_usage_report.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ImageUsageReportList:
    import aws_sdk_ec2.types.image_usage_report

    out: ImageUsageReportList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.image_usage_report.deserialize_ec2_query(child))
    return out

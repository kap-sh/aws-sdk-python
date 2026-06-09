"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_summary

AttributeSummaryList: TypeAlias = list[
    "aws_sdk_ec2.types.attribute_summary.AttributeSummary"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttributeSummaryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.attribute_summary

        aws_sdk_ec2.types.attribute_summary.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AttributeSummaryList:
    import aws_sdk_ec2.types.attribute_summary

    out: AttributeSummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.attribute_summary.deserialize_ec2_query(child))
    return out

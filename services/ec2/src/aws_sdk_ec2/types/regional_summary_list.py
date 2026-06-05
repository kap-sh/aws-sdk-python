"""Generated from Smithy shape ``com.amazonaws.ec2#RegionalSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.regional_summary

RegionalSummaryList: TypeAlias = list[
    "aws_sdk_ec2.types.regional_summary.RegionalSummary"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegionalSummaryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.regional_summary

        aws_sdk_ec2.types.regional_summary.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RegionalSummaryList:
    import aws_sdk_ec2.types.regional_summary

    out: RegionalSummaryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.regional_summary.deserialize_ec2_query(child))
    return out

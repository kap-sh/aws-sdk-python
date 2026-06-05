"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fleet_error

DescribeFleetsErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.describe_fleet_error.DescribeFleetError"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetsErrorSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.describe_fleet_error

        aws_sdk_ec2.types.describe_fleet_error.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> DescribeFleetsErrorSet:
    import aws_sdk_ec2.types.describe_fleet_error

    out: DescribeFleetsErrorSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.describe_fleet_error.deserialize_ec2_query(child))
    return out

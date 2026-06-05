"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchSpecsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_fleet_launch_specification

LaunchSpecsList: TypeAlias = list[
    "aws_sdk_ec2.types.spot_fleet_launch_specification.SpotFleetLaunchSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchSpecsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.spot_fleet_launch_specification

        aws_sdk_ec2.types.spot_fleet_launch_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LaunchSpecsList:
    import aws_sdk_ec2.types.spot_fleet_launch_specification

    out: LaunchSpecsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.spot_fleet_launch_specification.deserialize_ec2_query(
                child
            )
        )
    return out

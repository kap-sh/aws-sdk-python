"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_data

FleetSet: TypeAlias = list["aws_sdk_ec2.types.fleet_data.FleetData"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.fleet_data

        aws_sdk_ec2.types.fleet_data.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> FleetSet:
    import aws_sdk_ec2.types.fleet_data

    out: FleetSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.fleet_data.deserialize_ec2_query(child))
    return out

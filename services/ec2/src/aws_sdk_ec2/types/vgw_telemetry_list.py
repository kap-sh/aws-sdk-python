"""Generated from Smithy shape ``com.amazonaws.ec2#VgwTelemetryList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vgw_telemetry

VgwTelemetryList: TypeAlias = list["aws_sdk_ec2.types.vgw_telemetry.VgwTelemetry"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VgwTelemetryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.vgw_telemetry

        aws_sdk_ec2.types.vgw_telemetry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VgwTelemetryList:
    import aws_sdk_ec2.types.vgw_telemetry

    out: VgwTelemetryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.vgw_telemetry.deserialize_ec2_query(child))
    return out

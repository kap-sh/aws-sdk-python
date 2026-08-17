"""Generated from Smithy shape ``com.amazonaws.ec2#VgwTelemetryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vgw_telemetry

VgwTelemetryList: TypeAlias = list["capo_ec2.types.vgw_telemetry.VgwTelemetry"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VgwTelemetryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vgw_telemetry

        capo_ec2.types.vgw_telemetry.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> VgwTelemetryList:
    import capo_ec2.types.vgw_telemetry

    out: VgwTelemetryList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.vgw_telemetry.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VgwTelemetryList:
    import capo_ec2.types.vgw_telemetry

    out: VgwTelemetryList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vgw_telemetry.deserialize_ec2_query(child))
    return out

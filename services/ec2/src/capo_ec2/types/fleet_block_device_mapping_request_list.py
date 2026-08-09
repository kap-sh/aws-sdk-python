"""Generated from Smithy shape ``com.amazonaws.ec2#FleetBlockDeviceMappingRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_block_device_mapping_request

FleetBlockDeviceMappingRequestList: TypeAlias = list[
    "capo_ec2.types.fleet_block_device_mapping_request.FleetBlockDeviceMappingRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetBlockDeviceMappingRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fleet_block_device_mapping_request

        capo_ec2.types.fleet_block_device_mapping_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> FleetBlockDeviceMappingRequestList:
    import capo_ec2.types.fleet_block_device_mapping_request

    out: FleetBlockDeviceMappingRequestList = []
    for child in el.findall("BlockDeviceMapping"):
        out.append(
            capo_ec2.types.fleet_block_device_mapping_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FleetBlockDeviceMappingRequestList:
    import capo_ec2.types.fleet_block_device_mapping_request

    out: FleetBlockDeviceMappingRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.fleet_block_device_mapping_request.deserialize_ec2_query(
                child
            )
        )
    return out

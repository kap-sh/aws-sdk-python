"""Generated from Smithy shape ``com.amazonaws.storagegateway#VolumeiSCSIAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.integer
    import aws_sdk_storage_gateway.types.network_interface_id
    import aws_sdk_storage_gateway.types.positive_int_object
    import aws_sdk_storage_gateway.types.target_arn


class VolumeiSCSIAttributes(TypedDict):
    target_arn: NotRequired["aws_sdk_storage_gateway.types.target_arn.TargetARN"]
    """<p>The Amazon Resource Name (ARN) of the volume target.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_storage_gateway.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The network interface identifier.</p>"""
    network_interface_port: "aws_sdk_storage_gateway.types.integer.integer"
    """<p>The port used to communicate with iSCSI targets.</p>"""
    lun_number: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>The logical disk number.</p>"""
    chap_enabled: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>Indicates whether mutual CHAP is enabled for the iSCSI target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeiSCSIAttributes) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetARN"] = value["target_arn"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    out["NetworkInterfacePort"] = value.get("network_interface_port", 0)
    if "lun_number" in value:
        out["LunNumber"] = value["lun_number"]
    out["ChapEnabled"] = value.get("chap_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> VolumeiSCSIAttributes:
    out: VolumeiSCSIAttributes = {}  # type: ignore[typeddict-item]
    if "TargetARN" in data:
        out["target_arn"] = data["TargetARN"]
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if "NetworkInterfacePort" in data:
        out["network_interface_port"] = data["NetworkInterfacePort"]
    else:
        out["network_interface_port"] = 0
    if "LunNumber" in data:
        out["lun_number"] = data["LunNumber"]
    if "ChapEnabled" in data:
        out["chap_enabled"] = data["ChapEnabled"]
    else:
        out["chap_enabled"] = False
    return out

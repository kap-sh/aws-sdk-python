"""Generated from Smithy shape ``com.amazonaws.storagegateway#VTLDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.devicei_scsi_attributes
    import capo_storage_gateway.types.vtl_device_arn
    import capo_storage_gateway.types.vtl_device_product_identifier
    import capo_storage_gateway.types.vtl_device_type
    import capo_storage_gateway.types.vtl_device_vendor


class VTLDevice(TypedDict, closed=True):
    vtl_device_arn: NotRequired[
        "capo_storage_gateway.types.vtl_device_arn.VTLDeviceARN"
    ]
    """<p>Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media changer).</p>"""
    vtl_device_type: NotRequired[
        "capo_storage_gateway.types.vtl_device_type.VTLDeviceType"
    ]
    """<p>Specifies the type of device that the VTL device emulates.</p>"""
    vtl_device_vendor: NotRequired[
        "capo_storage_gateway.types.vtl_device_vendor.VTLDeviceVendor"
    ]
    """<p>Specifies the vendor of the device that the VTL device object emulates.</p>"""
    vtl_device_product_identifier: NotRequired[
        "capo_storage_gateway.types.vtl_device_product_identifier.VTLDeviceProductIdentifier"
    ]
    """<p>Specifies the model number of device that the VTL device emulates.</p>"""
    devicei_scsi_attributes: NotRequired[
        "capo_storage_gateway.types.devicei_scsi_attributes.DeviceiSCSIAttributes"
    ]
    """<p>A list of iSCSI information about a VTL device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VTLDevice) -> dict:
    out: dict = {}
    if "vtl_device_arn" in value:
        out["VTLDeviceARN"] = value["vtl_device_arn"]
    if "vtl_device_type" in value:
        out["VTLDeviceType"] = value["vtl_device_type"]
    if "vtl_device_vendor" in value:
        out["VTLDeviceVendor"] = value["vtl_device_vendor"]
    if "vtl_device_product_identifier" in value:
        out["VTLDeviceProductIdentifier"] = value["vtl_device_product_identifier"]
    if "devicei_scsi_attributes" in value:
        import capo_storage_gateway.types.devicei_scsi_attributes

        out["DeviceiSCSIAttributes"] = (
            capo_storage_gateway.types.devicei_scsi_attributes.serialize_aws_json_1_1(
                value["devicei_scsi_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VTLDevice:
    out: VTLDevice = {}  # type: ignore[typeddict-item]
    if "VTLDeviceARN" in data:
        out["vtl_device_arn"] = data["VTLDeviceARN"]
    if "VTLDeviceType" in data:
        out["vtl_device_type"] = data["VTLDeviceType"]
    if "VTLDeviceVendor" in data:
        out["vtl_device_vendor"] = data["VTLDeviceVendor"]
    if "VTLDeviceProductIdentifier" in data:
        out["vtl_device_product_identifier"] = data["VTLDeviceProductIdentifier"]
    if "DeviceiSCSIAttributes" in data:
        import capo_storage_gateway.types.devicei_scsi_attributes

        out["devicei_scsi_attributes"] = (
            capo_storage_gateway.types.devicei_scsi_attributes.deserialize_aws_json_1_1(
                data["DeviceiSCSIAttributes"]
            )
        )
    return out

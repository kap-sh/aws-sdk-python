"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateVTLDeviceTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.vtl_device_arn


class UpdateVTLDeviceTypeOutput(TypedDict, closed=True):
    vtl_device_arn: NotRequired[
        "aws_sdk_storage_gateway.types.vtl_device_arn.VTLDeviceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the medium changer you have selected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVTLDeviceTypeOutput) -> dict:
    out: dict = {}
    if "vtl_device_arn" in value:
        out["VTLDeviceARN"] = value["vtl_device_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVTLDeviceTypeOutput:
    out: UpdateVTLDeviceTypeOutput = {}  # type: ignore[typeddict-item]
    if "VTLDeviceARN" in data:
        out["vtl_device_arn"] = data["VTLDeviceARN"]
    return out

"""Generated from Smithy shape ``com.amazonaws.greengrass#Device``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__boolean
    import aws_sdk_greengrass.types.__string


class Device(TypedDict):
    certificate_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the certificate associated with the device."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''."""
    sync_shadow: NotRequired["aws_sdk_greengrass.types.__boolean.__boolean"]
    """If true, the device's local shadow will be automatically synced with the cloud."""
    thing_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The thing ARN of the device."""


# --- restJson1 ser/de ---
def serialize_json(value: Device) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "sync_shadow" in value:
        out["SyncShadow"] = value["sync_shadow"]
    if "thing_arn" in value:
        out["ThingArn"] = value["thing_arn"]
    return out


def deserialize_json(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "SyncShadow" in data:
        out["sync_shadow"] = data["SyncShadow"]
    if "ThingArn" in data:
        out["thing_arn"] = data["ThingArn"]
    return out

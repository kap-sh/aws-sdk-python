"""Generated from Smithy shape ``com.amazonaws.greengrass#Core``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__boolean
    import aws_sdk_greengrass.types.__string


class Core(TypedDict, closed=True):
    certificate_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the certificate associated with the core."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''."""
    sync_shadow: NotRequired["aws_sdk_greengrass.types.__boolean.__boolean"]
    """If true, the core's local shadow is automatically synced with the cloud."""
    thing_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the thing which is the core."""


# --- restJson1 ser/de ---
def serialize_json(value: Core) -> dict:
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


def deserialize_json(data: dict) -> Core:
    out: Core = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "SyncShadow" in data:
        out["sync_shadow"] = data["SyncShadow"]
    if "ThingArn" in data:
        out["thing_arn"] = data["ThingArn"]
    return out

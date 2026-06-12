"""Generated from Smithy shape ``com.amazonaws.panorama#OTAJobConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.boolean
    import aws_sdk_panorama.types.image_version


class OTAJobConfig(TypedDict):
    image_version: "aws_sdk_panorama.types.image_version.ImageVersion"
    """<p>The target version of the device software.</p>"""
    allow_major_version_update: "aws_sdk_panorama.types.boolean.Boolean"
    """<p>Whether to apply the update if it is a major version change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OTAJobConfig) -> dict:
    out: dict = {}
    out["ImageVersion"] = value["image_version"]
    out["AllowMajorVersionUpdate"] = value.get("allow_major_version_update", False)
    return out


def deserialize_json(data: dict) -> OTAJobConfig:
    out: OTAJobConfig = {}  # type: ignore[typeddict-item]
    if "ImageVersion" in data:
        out["image_version"] = data["ImageVersion"]
    else:
        raise DeserializationError("OTAJobConfig.image_version required")
    if "AllowMajorVersionUpdate" in data:
        out["allow_major_version_update"] = data["AllowMajorVersionUpdate"]
    else:
        out["allow_major_version_update"] = False
    return out

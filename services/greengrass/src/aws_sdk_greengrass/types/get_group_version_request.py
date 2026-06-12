"""Generated from Smithy shape ``com.amazonaws.greengrass#GetGroupVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetGroupVersionRequest(TypedDict):
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""
    group_version_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the group version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListGroupVersions'' requests. If the version is the last one that was associated with a group, the value also maps to the ''LatestVersion'' property of the corresponding ''GroupInformation'' object."""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGroupVersionRequest:
    out: GetGroupVersionRequest = {}  # type: ignore[typeddict-item]
    return out

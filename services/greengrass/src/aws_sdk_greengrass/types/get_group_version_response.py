"""Generated from Smithy shape ``com.amazonaws.greengrass#GetGroupVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.group_version


class GetGroupVersionResponse(TypedDict):
    arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the group version."""
    creation_timestamp: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the group version was created."""
    definition: NotRequired["aws_sdk_greengrass.types.group_version.GroupVersion"]
    """Information about the group version definition."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the group that the version is associated with."""
    version: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the group version."""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupVersionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    if "definition" in value:
        import aws_sdk_greengrass.types.group_version

        out["Definition"] = aws_sdk_greengrass.types.group_version.serialize_json(
            value["definition"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> GetGroupVersionResponse:
    out: GetGroupVersionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationTimestamp" in data:
        out["creation_timestamp"] = data["CreationTimestamp"]
    if "Definition" in data:
        import aws_sdk_greengrass.types.group_version

        out["definition"] = aws_sdk_greengrass.types.group_version.deserialize_json(
            data["Definition"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out

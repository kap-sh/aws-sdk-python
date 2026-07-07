"""Generated from Smithy shape ``com.amazonaws.greengrass#GetCoreDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.tags


class GetCoreDefinitionResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the definition."""
    creation_timestamp: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the definition was created."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the definition."""
    last_updated_timestamp: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the definition was last updated."""
    latest_version: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the latest version associated with the definition."""
    latest_version_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the latest version associated with the definition."""
    name: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the definition."""
    tags: NotRequired["aws_sdk_greengrass.types.tags.Tags"]
    """Tag(s) attached to the resource arn."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreDefinitionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    if "id" in value:
        out["Id"] = value["id"]
    if "last_updated_timestamp" in value:
        out["LastUpdatedTimestamp"] = value["last_updated_timestamp"]
    if "latest_version" in value:
        out["LatestVersion"] = value["latest_version"]
    if "latest_version_arn" in value:
        out["LatestVersionArn"] = value["latest_version_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_greengrass.types.tags

        out["tags"] = aws_sdk_greengrass.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCoreDefinitionResponse:
    out: GetCoreDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationTimestamp" in data:
        out["creation_timestamp"] = data["CreationTimestamp"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "LastUpdatedTimestamp" in data:
        out["last_updated_timestamp"] = data["LastUpdatedTimestamp"]
    if "LatestVersion" in data:
        out["latest_version"] = data["LatestVersion"]
    if "LatestVersionArn" in data:
        out["latest_version_arn"] = data["LatestVersionArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "tags" in data:
        import aws_sdk_greengrass.types.tags

        out["tags"] = aws_sdk_greengrass.types.tags.deserialize_json(data["tags"])
    return out

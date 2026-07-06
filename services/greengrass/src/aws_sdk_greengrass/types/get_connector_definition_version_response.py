"""Generated from Smithy shape ``com.amazonaws.greengrass#GetConnectorDefinitionVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.connector_definition_version


class GetConnectorDefinitionVersionResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the connector definition version."""
    creation_timestamp: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the connector definition version was created."""
    definition: NotRequired[
        "aws_sdk_greengrass.types.connector_definition_version.ConnectorDefinitionVersion"
    ]
    """Information about the connector definition version."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the connector definition version."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""
    version: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The version of the connector definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorDefinitionVersionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    if "definition" in value:
        import aws_sdk_greengrass.types.connector_definition_version

        out["Definition"] = (
            aws_sdk_greengrass.types.connector_definition_version.serialize_json(
                value["definition"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> GetConnectorDefinitionVersionResponse:
    out: GetConnectorDefinitionVersionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationTimestamp" in data:
        out["creation_timestamp"] = data["CreationTimestamp"]
    if "Definition" in data:
        import aws_sdk_greengrass.types.connector_definition_version

        out["definition"] = (
            aws_sdk_greengrass.types.connector_definition_version.deserialize_json(
                data["Definition"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out

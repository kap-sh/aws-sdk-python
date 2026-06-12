"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateCoreDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.core_definition_version
    import aws_sdk_greengrass.types.tags


class CreateCoreDefinitionRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    initial_version: NotRequired[
        "aws_sdk_greengrass.types.core_definition_version.CoreDefinitionVersion"
    ]
    """Information about the initial version of the core definition."""
    name: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the core definition."""
    tags: NotRequired["aws_sdk_greengrass.types.tags.Tags"]
    """Tag(s) to add to the new resource."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreDefinitionRequest) -> dict:
    out: dict = {}
    if "initial_version" in value:
        import aws_sdk_greengrass.types.core_definition_version

        out["InitialVersion"] = (
            aws_sdk_greengrass.types.core_definition_version.serialize_json(
                value["initial_version"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_greengrass.types.tags

        out["tags"] = aws_sdk_greengrass.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCoreDefinitionRequest:
    out: CreateCoreDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "InitialVersion" in data:
        import aws_sdk_greengrass.types.core_definition_version

        out["initial_version"] = (
            aws_sdk_greengrass.types.core_definition_version.deserialize_json(
                data["InitialVersion"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "tags" in data:
        import aws_sdk_greengrass.types.tags

        out["tags"] = aws_sdk_greengrass.types.tags.deserialize_json(data["tags"])
    return out

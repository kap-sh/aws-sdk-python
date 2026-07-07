"""Generated from Smithy shape ``com.amazonaws.securityagent#ProviderResourceCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.git_hub_resource_capabilities


class _ProviderResourceCapabilities_github(TypedDict, closed=True):
    github: "aws_sdk_securityagent.types.git_hub_resource_capabilities.GitHubResourceCapabilities"


ProviderResourceCapabilities: TypeAlias = _ProviderResourceCapabilities_github


# --- restJson1 ser/de ---
def serialize_json(value: ProviderResourceCapabilities) -> dict:
    if "github" in value:
        import aws_sdk_securityagent.types.git_hub_resource_capabilities

        return {
            "github": aws_sdk_securityagent.types.git_hub_resource_capabilities.serialize_json(
                value["github"]
            )
        }
    else:
        raise SerializationError("ProviderResourceCapabilities: no variant present")


def deserialize_json(data: dict) -> ProviderResourceCapabilities:
    if "github" in data:
        import aws_sdk_securityagent.types.git_hub_resource_capabilities

        return {
            "github": aws_sdk_securityagent.types.git_hub_resource_capabilities.deserialize_json(
                data["github"]
            )
        }
    else:
        raise DeserializationError(
            "ProviderResourceCapabilities: no recognized variant key"
        )

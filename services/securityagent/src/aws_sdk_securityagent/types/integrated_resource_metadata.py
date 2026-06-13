"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.git_hub_repository_metadata


class _IntegratedResourceMetadata_githubRepository(TypedDict):
    githubRepository: "aws_sdk_securityagent.types.git_hub_repository_metadata.GitHubRepositoryMetadata"


IntegratedResourceMetadata: TypeAlias = _IntegratedResourceMetadata_githubRepository


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceMetadata) -> dict:
    if "githubRepository" in value:
        import aws_sdk_securityagent.types.git_hub_repository_metadata

        return {
            "githubRepository": aws_sdk_securityagent.types.git_hub_repository_metadata.serialize_json(
                value["githubRepository"]
            )
        }
    else:
        raise SerializationError("IntegratedResourceMetadata: no variant present")


def deserialize_json(data: dict) -> IntegratedResourceMetadata:
    if "githubRepository" in data:
        import aws_sdk_securityagent.types.git_hub_repository_metadata

        return {
            "githubRepository": aws_sdk_securityagent.types.git_hub_repository_metadata.deserialize_json(
                data["githubRepository"]
            )
        }
    else:
        raise DeserializationError(
            "IntegratedResourceMetadata: no recognized variant key"
        )

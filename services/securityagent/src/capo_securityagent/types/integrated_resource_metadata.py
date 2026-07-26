"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.git_hub_repository_metadata


class _IntegratedResourceMetadata_githubRepository(TypedDict, closed=True):
    githubRepository: (
        "capo_securityagent.types.git_hub_repository_metadata.GitHubRepositoryMetadata"
    )


IntegratedResourceMetadata: TypeAlias = _IntegratedResourceMetadata_githubRepository


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceMetadata) -> dict:
    if "githubRepository" in value:
        import capo_securityagent.types.git_hub_repository_metadata

        return {
            "githubRepository": capo_securityagent.types.git_hub_repository_metadata.serialize_json(
                value["githubRepository"]
            )
        }
    else:
        raise SerializationError("IntegratedResourceMetadata: no variant present")


def deserialize_json(data: dict) -> IntegratedResourceMetadata:
    if "githubRepository" in data:
        import capo_securityagent.types.git_hub_repository_metadata

        return {
            "githubRepository": capo_securityagent.types.git_hub_repository_metadata.deserialize_json(
                data["githubRepository"]
            )
        }
    else:
        raise DeserializationError(
            "IntegratedResourceMetadata: no recognized variant key"
        )

"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.git_hub_repository_resource


class _IntegratedResource_githubRepository(TypedDict, closed=True):
    githubRepository: "aws_sdk_securityagent.types.git_hub_repository_resource.GitHubRepositoryResource"


IntegratedResource: TypeAlias = _IntegratedResource_githubRepository


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResource) -> dict:
    if "githubRepository" in value:
        import aws_sdk_securityagent.types.git_hub_repository_resource

        return {
            "githubRepository": aws_sdk_securityagent.types.git_hub_repository_resource.serialize_json(
                value["githubRepository"]
            )
        }
    else:
        raise SerializationError("IntegratedResource: no variant present")


def deserialize_json(data: dict) -> IntegratedResource:
    if "githubRepository" in data:
        import aws_sdk_securityagent.types.git_hub_repository_resource

        return {
            "githubRepository": aws_sdk_securityagent.types.git_hub_repository_resource.deserialize_json(
                data["githubRepository"]
            )
        }
    else:
        raise DeserializationError("IntegratedResource: no recognized variant key")

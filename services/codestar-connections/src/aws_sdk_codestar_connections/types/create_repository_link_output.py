"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateRepositoryLinkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.repository_link_info


class CreateRepositoryLinkOutput(TypedDict, closed=True):
    repository_link_info: (
        "aws_sdk_codestar_connections.types.repository_link_info.RepositoryLinkInfo"
    )
    """<p>The returned information about the created repository link.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRepositoryLinkOutput) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.repository_link_info

    out["RepositoryLinkInfo"] = (
        aws_sdk_codestar_connections.types.repository_link_info.serialize_aws_json_1_0(
            value["repository_link_info"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRepositoryLinkOutput:
    out: CreateRepositoryLinkOutput = {}  # type: ignore[typeddict-item]
    if "RepositoryLinkInfo" in data:
        import aws_sdk_codestar_connections.types.repository_link_info

        out["repository_link_info"] = (
            aws_sdk_codestar_connections.types.repository_link_info.deserialize_aws_json_1_0(
                data["RepositoryLinkInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRepositoryLinkOutput.repository_link_info required"
        )
    return out

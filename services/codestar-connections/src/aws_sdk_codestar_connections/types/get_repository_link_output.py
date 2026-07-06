"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetRepositoryLinkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.repository_link_info


class GetRepositoryLinkOutput(TypedDict, closed=True):
    repository_link_info: (
        "aws_sdk_codestar_connections.types.repository_link_info.RepositoryLinkInfo"
    )
    """<p>The information returned for a specified repository link.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositoryLinkOutput) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.repository_link_info

    out["RepositoryLinkInfo"] = (
        aws_sdk_codestar_connections.types.repository_link_info.serialize_aws_json_1_0(
            value["repository_link_info"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositoryLinkOutput:
    out: GetRepositoryLinkOutput = {}  # type: ignore[typeddict-item]
    if "RepositoryLinkInfo" in data:
        import aws_sdk_codestar_connections.types.repository_link_info

        out["repository_link_info"] = (
            aws_sdk_codestar_connections.types.repository_link_info.deserialize_aws_json_1_0(
                data["RepositoryLinkInfo"]
            )
        )
    else:
        raise DeserializationError(
            "GetRepositoryLinkOutput.repository_link_info required"
        )
    return out

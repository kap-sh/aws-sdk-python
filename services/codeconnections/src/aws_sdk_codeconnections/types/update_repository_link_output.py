"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateRepositoryLinkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.repository_link_info


class UpdateRepositoryLinkOutput(TypedDict, closed=True):
    repository_link_info: (
        "aws_sdk_codeconnections.types.repository_link_info.RepositoryLinkInfo"
    )
    """<p>Information about the repository link to be updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRepositoryLinkOutput) -> dict:
    out: dict = {}
    import aws_sdk_codeconnections.types.repository_link_info

    out["RepositoryLinkInfo"] = (
        aws_sdk_codeconnections.types.repository_link_info.serialize_aws_json_1_0(
            value["repository_link_info"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRepositoryLinkOutput:
    out: UpdateRepositoryLinkOutput = {}  # type: ignore[typeddict-item]
    if "RepositoryLinkInfo" in data:
        import aws_sdk_codeconnections.types.repository_link_info

        out["repository_link_info"] = (
            aws_sdk_codeconnections.types.repository_link_info.deserialize_aws_json_1_0(
                data["RepositoryLinkInfo"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRepositoryLinkOutput.repository_link_info required"
        )
    return out

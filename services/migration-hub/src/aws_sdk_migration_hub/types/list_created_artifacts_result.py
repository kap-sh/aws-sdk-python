"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListCreatedArtifactsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.created_artifact_list
    import aws_sdk_migration_hub.types.token


class ListCreatedArtifactsResult(TypedDict):
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If there are more created artifacts than the max result, return the next token to be passed to the next call as a bookmark of where to start from.</p>"""
    created_artifact_list: NotRequired[
        "aws_sdk_migration_hub.types.created_artifact_list.CreatedArtifactList"
    ]
    """<p>List of created artifacts up to the maximum number of results specified in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCreatedArtifactsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "created_artifact_list" in value:
        import aws_sdk_migration_hub.types.created_artifact_list

        out["CreatedArtifactList"] = (
            aws_sdk_migration_hub.types.created_artifact_list.serialize_aws_json_1_1(
                value["created_artifact_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCreatedArtifactsResult:
    out: ListCreatedArtifactsResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "CreatedArtifactList" in data:
        import aws_sdk_migration_hub.types.created_artifact_list

        out["created_artifact_list"] = (
            aws_sdk_migration_hub.types.created_artifact_list.deserialize_aws_json_1_1(
                data["CreatedArtifactList"]
            )
        )
    return out

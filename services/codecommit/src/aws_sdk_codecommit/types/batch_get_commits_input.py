"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetCommitsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit_ids_input_list
    import aws_sdk_codecommit.types.repository_name


class BatchGetCommitsInput(TypedDict, closed=True):
    commit_ids: "aws_sdk_codecommit.types.commit_ids_input_list.CommitIdsInputList"
    """<p>The full commit IDs of the commits to get information about.</p> <note> <p>You must supply the full SHA IDs of each commit. You cannot use shortened SHA IDs.</p> </note>"""
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the commits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCommitsInput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.commit_ids_input_list

    out["commitIds"] = (
        aws_sdk_codecommit.types.commit_ids_input_list.serialize_aws_json_1_1(
            value["commit_ids"]
        )
    )
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCommitsInput:
    out: BatchGetCommitsInput = {}  # type: ignore[typeddict-item]
    if "commitIds" in data:
        import aws_sdk_codecommit.types.commit_ids_input_list

        out["commit_ids"] = (
            aws_sdk_codecommit.types.commit_ids_input_list.deserialize_aws_json_1_1(
                data["commitIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetCommitsInput.commit_ids required")
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("BatchGetCommitsInput.repository_name required")
    return out

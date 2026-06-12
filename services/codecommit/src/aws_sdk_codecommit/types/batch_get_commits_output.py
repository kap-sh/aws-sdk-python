"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetCommitsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.batch_get_commits_errors_list
    import aws_sdk_codecommit.types.commit_objects_list


class BatchGetCommitsOutput(TypedDict):
    commits: NotRequired[
        "aws_sdk_codecommit.types.commit_objects_list.CommitObjectsList"
    ]
    """<p>An array of commit data type objects, each of which contains information about a specified commit.</p>"""
    errors: NotRequired[
        "aws_sdk_codecommit.types.batch_get_commits_errors_list.BatchGetCommitsErrorsList"
    ]
    """<p>Returns any commit IDs for which information could not be found. For example, if one of the commit IDs was a shortened SHA ID or that commit was not found in the specified repository, the ID returns an error object with more information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCommitsOutput) -> dict:
    out: dict = {}
    if "commits" in value:
        import aws_sdk_codecommit.types.commit_objects_list

        out["commits"] = (
            aws_sdk_codecommit.types.commit_objects_list.serialize_aws_json_1_1(
                value["commits"]
            )
        )
    if "errors" in value:
        import aws_sdk_codecommit.types.batch_get_commits_errors_list

        out["errors"] = (
            aws_sdk_codecommit.types.batch_get_commits_errors_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCommitsOutput:
    out: BatchGetCommitsOutput = {}  # type: ignore[typeddict-item]
    if "commits" in data:
        import aws_sdk_codecommit.types.commit_objects_list

        out["commits"] = (
            aws_sdk_codecommit.types.commit_objects_list.deserialize_aws_json_1_1(
                data["commits"]
            )
        )
    if "errors" in data:
        import aws_sdk_codecommit.types.batch_get_commits_errors_list

        out["errors"] = (
            aws_sdk_codecommit.types.batch_get_commits_errors_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out

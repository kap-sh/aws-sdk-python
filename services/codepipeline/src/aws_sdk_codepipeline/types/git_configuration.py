"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_name
    import aws_sdk_codepipeline.types.git_pull_request_filter_list
    import aws_sdk_codepipeline.types.git_push_filter_list


class GitConfiguration(TypedDict):
    source_action_name: "aws_sdk_codepipeline.types.action_name.ActionName"
    """<p>The name of the pipeline source action where the trigger configuration, such as Git tags, is specified. The trigger configuration will start the pipeline upon the specified change only.</p> <note> <p>You can only specify one trigger configuration per source action.</p> </note>"""
    push: NotRequired[
        "aws_sdk_codepipeline.types.git_push_filter_list.GitPushFilterList"
    ]
    """<p>The field where the repository event that will start the pipeline, such as pushing Git tags, is specified with details.</p>"""
    pull_request: NotRequired[
        "aws_sdk_codepipeline.types.git_pull_request_filter_list.GitPullRequestFilterList"
    ]
    """<p>The field where the repository event that will start the pipeline is specified as pull requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitConfiguration) -> dict:
    out: dict = {}
    out["sourceActionName"] = value["source_action_name"]
    if "push" in value:
        import aws_sdk_codepipeline.types.git_push_filter_list

        out["push"] = (
            aws_sdk_codepipeline.types.git_push_filter_list.serialize_aws_json_1_1(
                value["push"]
            )
        )
    if "pull_request" in value:
        import aws_sdk_codepipeline.types.git_pull_request_filter_list

        out["pullRequest"] = (
            aws_sdk_codepipeline.types.git_pull_request_filter_list.serialize_aws_json_1_1(
                value["pull_request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitConfiguration:
    out: GitConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceActionName" in data:
        out["source_action_name"] = data["sourceActionName"]
    else:
        raise DeserializationError("GitConfiguration.source_action_name required")
    if "push" in data:
        import aws_sdk_codepipeline.types.git_push_filter_list

        out["push"] = (
            aws_sdk_codepipeline.types.git_push_filter_list.deserialize_aws_json_1_1(
                data["push"]
            )
        )
    if "pullRequest" in data:
        import aws_sdk_codepipeline.types.git_pull_request_filter_list

        out["pull_request"] = (
            aws_sdk_codepipeline.types.git_pull_request_filter_list.deserialize_aws_json_1_1(
                data["pullRequest"]
            )
        )
    return out

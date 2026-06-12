"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggerExecutionFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_trigger_execution_failure_message
    import aws_sdk_codecommit.types.repository_trigger_name


class RepositoryTriggerExecutionFailure(TypedDict):
    trigger: NotRequired[
        "aws_sdk_codecommit.types.repository_trigger_name.RepositoryTriggerName"
    ]
    """<p>The name of the trigger that did not run.</p>"""
    failure_message: NotRequired[
        "aws_sdk_codecommit.types.repository_trigger_execution_failure_message.RepositoryTriggerExecutionFailureMessage"
    ]
    """<p>Message information about the trigger that did not run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTriggerExecutionFailure) -> dict:
    out: dict = {}
    if "trigger" in value:
        out["trigger"] = value["trigger"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryTriggerExecutionFailure:
    out: RepositoryTriggerExecutionFailure = {}  # type: ignore[typeddict-item]
    if "trigger" in data:
        out["trigger"] = data["trigger"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out

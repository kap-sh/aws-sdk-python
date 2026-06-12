"""Generated from Smithy shape ``com.amazonaws.codecommit#TestRepositoryTriggersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_trigger_execution_failure_list
    import aws_sdk_codecommit.types.repository_trigger_name_list


class TestRepositoryTriggersOutput(TypedDict):
    successful_executions: NotRequired[
        "aws_sdk_codecommit.types.repository_trigger_name_list.RepositoryTriggerNameList"
    ]
    """<p>The list of triggers that were successfully tested. This list provides the names of the triggers that were successfully tested, separated by commas.</p>"""
    failed_executions: NotRequired[
        "aws_sdk_codecommit.types.repository_trigger_execution_failure_list.RepositoryTriggerExecutionFailureList"
    ]
    """<p>The list of triggers that were not tested. This list provides the names of the triggers that could not be tested, separated by commas.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestRepositoryTriggersOutput) -> dict:
    out: dict = {}
    if "successful_executions" in value:
        import aws_sdk_codecommit.types.repository_trigger_name_list

        out["successfulExecutions"] = (
            aws_sdk_codecommit.types.repository_trigger_name_list.serialize_aws_json_1_1(
                value["successful_executions"]
            )
        )
    if "failed_executions" in value:
        import aws_sdk_codecommit.types.repository_trigger_execution_failure_list

        out["failedExecutions"] = (
            aws_sdk_codecommit.types.repository_trigger_execution_failure_list.serialize_aws_json_1_1(
                value["failed_executions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestRepositoryTriggersOutput:
    out: TestRepositoryTriggersOutput = {}  # type: ignore[typeddict-item]
    if "successfulExecutions" in data:
        import aws_sdk_codecommit.types.repository_trigger_name_list

        out["successful_executions"] = (
            aws_sdk_codecommit.types.repository_trigger_name_list.deserialize_aws_json_1_1(
                data["successfulExecutions"]
            )
        )
    if "failedExecutions" in data:
        import aws_sdk_codecommit.types.repository_trigger_execution_failure_list

        out["failed_executions"] = (
            aws_sdk_codecommit.types.repository_trigger_execution_failure_list.deserialize_aws_json_1_1(
                data["failedExecutions"]
            )
        )
    return out

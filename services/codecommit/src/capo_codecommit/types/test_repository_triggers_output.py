"""Generated from Smithy shape ``com.amazonaws.codecommit#TestRepositoryTriggersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_trigger_execution_failure_list
    import capo_codecommit.types.repository_trigger_name_list


class TestRepositoryTriggersOutput(TypedDict, closed=True):
    successful_executions: NotRequired[
        "capo_codecommit.types.repository_trigger_name_list.RepositoryTriggerNameList"
    ]
    """<p>The list of triggers that were successfully tested. This list provides the names of the triggers that were successfully tested, separated by commas.</p>"""
    failed_executions: NotRequired[
        "capo_codecommit.types.repository_trigger_execution_failure_list.RepositoryTriggerExecutionFailureList"
    ]
    """<p>The list of triggers that were not tested. This list provides the names of the triggers that could not be tested, separated by commas.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestRepositoryTriggersOutput) -> dict:
    out: dict = {}
    if "successful_executions" in value:
        import capo_codecommit.types.repository_trigger_name_list

        out["successfulExecutions"] = (
            capo_codecommit.types.repository_trigger_name_list.serialize_aws_json_1_1(
                value["successful_executions"]
            )
        )
    if "failed_executions" in value:
        import capo_codecommit.types.repository_trigger_execution_failure_list

        out["failedExecutions"] = (
            capo_codecommit.types.repository_trigger_execution_failure_list.serialize_aws_json_1_1(
                value["failed_executions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestRepositoryTriggersOutput:
    out: TestRepositoryTriggersOutput = {}  # type: ignore[typeddict-item]
    if "successfulExecutions" in data:
        import capo_codecommit.types.repository_trigger_name_list

        out["successful_executions"] = (
            capo_codecommit.types.repository_trigger_name_list.deserialize_aws_json_1_1(
                data["successfulExecutions"]
            )
        )
    if "failedExecutions" in data:
        import capo_codecommit.types.repository_trigger_execution_failure_list

        out["failed_executions"] = (
            capo_codecommit.types.repository_trigger_execution_failure_list.deserialize_aws_json_1_1(
                data["failedExecutions"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_state_list
    import aws_sdk_codepipeline.types.retry_stage_metadata
    import aws_sdk_codepipeline.types.stage_condition_state
    import aws_sdk_codepipeline.types.stage_execution
    import aws_sdk_codepipeline.types.stage_execution_list
    import aws_sdk_codepipeline.types.stage_name
    import aws_sdk_codepipeline.types.transition_state


class StageState(TypedDict):
    stage_name: NotRequired["aws_sdk_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage.</p>"""
    inbound_execution: NotRequired[
        "aws_sdk_codepipeline.types.stage_execution.StageExecution"
    ]
    inbound_executions: NotRequired[
        "aws_sdk_codepipeline.types.stage_execution_list.StageExecutionList"
    ]
    """<p>The inbound executions for a stage.</p>"""
    inbound_transition_state: NotRequired[
        "aws_sdk_codepipeline.types.transition_state.TransitionState"
    ]
    """<p>The state of the inbound transition, which is either enabled or disabled.</p>"""
    action_states: NotRequired[
        "aws_sdk_codepipeline.types.action_state_list.ActionStateList"
    ]
    """<p>The state of the stage.</p>"""
    latest_execution: NotRequired[
        "aws_sdk_codepipeline.types.stage_execution.StageExecution"
    ]
    """<p>Information about the latest execution in the stage, including its ID and status.</p>"""
    before_entry_condition_state: NotRequired[
        "aws_sdk_codepipeline.types.stage_condition_state.StageConditionState"
    ]
    """<p>The state of the entry conditions for a stage.</p>"""
    on_success_condition_state: NotRequired[
        "aws_sdk_codepipeline.types.stage_condition_state.StageConditionState"
    ]
    """<p>The state of the success conditions for a stage.</p>"""
    on_failure_condition_state: NotRequired[
        "aws_sdk_codepipeline.types.stage_condition_state.StageConditionState"
    ]
    """<p>The state of the failure conditions for a stage.</p>"""
    retry_stage_metadata: NotRequired[
        "aws_sdk_codepipeline.types.retry_stage_metadata.RetryStageMetadata"
    ]
    """<p>he details of a specific automatic retry on stage failure, including the attempt number and trigger.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageState) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "inbound_execution" in value:
        import aws_sdk_codepipeline.types.stage_execution

        out["inboundExecution"] = (
            aws_sdk_codepipeline.types.stage_execution.serialize_aws_json_1_1(
                value["inbound_execution"]
            )
        )
    if "inbound_executions" in value:
        import aws_sdk_codepipeline.types.stage_execution_list

        out["inboundExecutions"] = (
            aws_sdk_codepipeline.types.stage_execution_list.serialize_aws_json_1_1(
                value["inbound_executions"]
            )
        )
    if "inbound_transition_state" in value:
        import aws_sdk_codepipeline.types.transition_state

        out["inboundTransitionState"] = (
            aws_sdk_codepipeline.types.transition_state.serialize_aws_json_1_1(
                value["inbound_transition_state"]
            )
        )
    if "action_states" in value:
        import aws_sdk_codepipeline.types.action_state_list

        out["actionStates"] = (
            aws_sdk_codepipeline.types.action_state_list.serialize_aws_json_1_1(
                value["action_states"]
            )
        )
    if "latest_execution" in value:
        import aws_sdk_codepipeline.types.stage_execution

        out["latestExecution"] = (
            aws_sdk_codepipeline.types.stage_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "before_entry_condition_state" in value:
        import aws_sdk_codepipeline.types.stage_condition_state

        out["beforeEntryConditionState"] = (
            aws_sdk_codepipeline.types.stage_condition_state.serialize_aws_json_1_1(
                value["before_entry_condition_state"]
            )
        )
    if "on_success_condition_state" in value:
        import aws_sdk_codepipeline.types.stage_condition_state

        out["onSuccessConditionState"] = (
            aws_sdk_codepipeline.types.stage_condition_state.serialize_aws_json_1_1(
                value["on_success_condition_state"]
            )
        )
    if "on_failure_condition_state" in value:
        import aws_sdk_codepipeline.types.stage_condition_state

        out["onFailureConditionState"] = (
            aws_sdk_codepipeline.types.stage_condition_state.serialize_aws_json_1_1(
                value["on_failure_condition_state"]
            )
        )
    if "retry_stage_metadata" in value:
        import aws_sdk_codepipeline.types.retry_stage_metadata

        out["retryStageMetadata"] = (
            aws_sdk_codepipeline.types.retry_stage_metadata.serialize_aws_json_1_1(
                value["retry_stage_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StageState:
    out: StageState = {}  # type: ignore[typeddict-item]
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    if "inboundExecution" in data:
        import aws_sdk_codepipeline.types.stage_execution

        out["inbound_execution"] = (
            aws_sdk_codepipeline.types.stage_execution.deserialize_aws_json_1_1(
                data["inboundExecution"]
            )
        )
    if "inboundExecutions" in data:
        import aws_sdk_codepipeline.types.stage_execution_list

        out["inbound_executions"] = (
            aws_sdk_codepipeline.types.stage_execution_list.deserialize_aws_json_1_1(
                data["inboundExecutions"]
            )
        )
    if "inboundTransitionState" in data:
        import aws_sdk_codepipeline.types.transition_state

        out["inbound_transition_state"] = (
            aws_sdk_codepipeline.types.transition_state.deserialize_aws_json_1_1(
                data["inboundTransitionState"]
            )
        )
    if "actionStates" in data:
        import aws_sdk_codepipeline.types.action_state_list

        out["action_states"] = (
            aws_sdk_codepipeline.types.action_state_list.deserialize_aws_json_1_1(
                data["actionStates"]
            )
        )
    if "latestExecution" in data:
        import aws_sdk_codepipeline.types.stage_execution

        out["latest_execution"] = (
            aws_sdk_codepipeline.types.stage_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if "beforeEntryConditionState" in data:
        import aws_sdk_codepipeline.types.stage_condition_state

        out["before_entry_condition_state"] = (
            aws_sdk_codepipeline.types.stage_condition_state.deserialize_aws_json_1_1(
                data["beforeEntryConditionState"]
            )
        )
    if "onSuccessConditionState" in data:
        import aws_sdk_codepipeline.types.stage_condition_state

        out["on_success_condition_state"] = (
            aws_sdk_codepipeline.types.stage_condition_state.deserialize_aws_json_1_1(
                data["onSuccessConditionState"]
            )
        )
    if "onFailureConditionState" in data:
        import aws_sdk_codepipeline.types.stage_condition_state

        out["on_failure_condition_state"] = (
            aws_sdk_codepipeline.types.stage_condition_state.deserialize_aws_json_1_1(
                data["onFailureConditionState"]
            )
        )
    if "retryStageMetadata" in data:
        import aws_sdk_codepipeline.types.retry_stage_metadata

        out["retry_stage_metadata"] = (
            aws_sdk_codepipeline.types.retry_stage_metadata.deserialize_aws_json_1_1(
                data["retryStageMetadata"]
            )
        )
    return out

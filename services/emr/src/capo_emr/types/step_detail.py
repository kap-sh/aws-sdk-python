"""Generated from Smithy shape ``com.amazonaws.emr#StepDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.step_config
    import capo_emr.types.step_execution_status_detail


class StepDetail(TypedDict, closed=True):
    step_config: NotRequired["capo_emr.types.step_config.StepConfig"]
    """<p>The step configuration.</p>"""
    execution_status_detail: NotRequired[
        "capo_emr.types.step_execution_status_detail.StepExecutionStatusDetail"
    ]
    """<p>The description of the step status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepDetail) -> dict:
    out: dict = {}
    if "step_config" in value:
        import capo_emr.types.step_config

        out["StepConfig"] = capo_emr.types.step_config.serialize_aws_json_1_1(
            value["step_config"]
        )
    if "execution_status_detail" in value:
        import capo_emr.types.step_execution_status_detail

        out["ExecutionStatusDetail"] = (
            capo_emr.types.step_execution_status_detail.serialize_aws_json_1_1(
                value["execution_status_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepDetail:
    out: StepDetail = {}  # type: ignore[typeddict-item]
    if "StepConfig" in data:
        import capo_emr.types.step_config

        out["step_config"] = capo_emr.types.step_config.deserialize_aws_json_1_1(
            data["StepConfig"]
        )
    if "ExecutionStatusDetail" in data:
        import capo_emr.types.step_execution_status_detail

        out["execution_status_detail"] = (
            capo_emr.types.step_execution_status_detail.deserialize_aws_json_1_1(
                data["ExecutionStatusDetail"]
            )
        )
    return out

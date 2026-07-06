"""Generated from Smithy shape ``com.amazonaws.emr#StepDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.step_config
    import aws_sdk_emr.types.step_execution_status_detail


class StepDetail(TypedDict, closed=True):
    step_config: NotRequired["aws_sdk_emr.types.step_config.StepConfig"]
    """<p>The step configuration.</p>"""
    execution_status_detail: NotRequired[
        "aws_sdk_emr.types.step_execution_status_detail.StepExecutionStatusDetail"
    ]
    """<p>The description of the step status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepDetail) -> dict:
    out: dict = {}
    if "step_config" in value:
        import aws_sdk_emr.types.step_config

        out["StepConfig"] = aws_sdk_emr.types.step_config.serialize_aws_json_1_1(
            value["step_config"]
        )
    if "execution_status_detail" in value:
        import aws_sdk_emr.types.step_execution_status_detail

        out["ExecutionStatusDetail"] = (
            aws_sdk_emr.types.step_execution_status_detail.serialize_aws_json_1_1(
                value["execution_status_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepDetail:
    out: StepDetail = {}  # type: ignore[typeddict-item]
    if "StepConfig" in data:
        import aws_sdk_emr.types.step_config

        out["step_config"] = aws_sdk_emr.types.step_config.deserialize_aws_json_1_1(
            data["StepConfig"]
        )
    if "ExecutionStatusDetail" in data:
        import aws_sdk_emr.types.step_execution_status_detail

        out["execution_status_detail"] = (
            aws_sdk_emr.types.step_execution_status_detail.deserialize_aws_json_1_1(
                data["ExecutionStatusDetail"]
            )
        )
    return out

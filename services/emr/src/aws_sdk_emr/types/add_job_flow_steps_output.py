"""Generated from Smithy shape ``com.amazonaws.emr#AddJobFlowStepsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.step_ids_list


class AddJobFlowStepsOutput(TypedDict, closed=True):
    step_ids: NotRequired["aws_sdk_emr.types.step_ids_list.StepIdsList"]
    """<p>The identifiers of the list of steps added to the job flow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddJobFlowStepsOutput) -> dict:
    out: dict = {}
    if "step_ids" in value:
        import aws_sdk_emr.types.step_ids_list

        out["StepIds"] = aws_sdk_emr.types.step_ids_list.serialize_aws_json_1_1(
            value["step_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddJobFlowStepsOutput:
    out: AddJobFlowStepsOutput = {}  # type: ignore[typeddict-item]
    if "StepIds" in data:
        import aws_sdk_emr.types.step_ids_list

        out["step_ids"] = aws_sdk_emr.types.step_ids_list.deserialize_aws_json_1_1(
            data["StepIds"]
        )
    return out

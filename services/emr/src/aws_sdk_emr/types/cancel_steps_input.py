"""Generated from Smithy shape ``com.amazonaws.emr#CancelStepsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.step_cancellation_option
    import aws_sdk_emr.types.step_ids_list
    import aws_sdk_emr.types.xml_string_max_len256


class CancelStepsInput(TypedDict, closed=True):
    cluster_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The <code>ClusterID</code> for the specified steps that will be canceled. Use <a>RunJobFlow</a> and <a>ListClusters</a> to get ClusterIDs. </p>"""
    step_ids: NotRequired["aws_sdk_emr.types.step_ids_list.StepIdsList"]
    """<p>The list of <code>StepIDs</code> to cancel. Use <a>ListSteps</a> to get steps and their states for the specified cluster.</p>"""
    step_cancellation_option: NotRequired[
        "aws_sdk_emr.types.step_cancellation_option.StepCancellationOption"
    ]
    """<p>The option to choose to cancel <code>RUNNING</code> steps. By default, the value is <code>SEND_INTERRUPT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStepsInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "step_ids" in value:
        import aws_sdk_emr.types.step_ids_list

        out["StepIds"] = aws_sdk_emr.types.step_ids_list.serialize_aws_json_1_1(
            value["step_ids"]
        )
    if "step_cancellation_option" in value:
        import aws_sdk_emr.types.step_cancellation_option

        out["StepCancellationOption"] = (
            aws_sdk_emr.types.step_cancellation_option.serialize_aws_json_1_1(
                value["step_cancellation_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelStepsInput:
    out: CancelStepsInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "StepIds" in data:
        import aws_sdk_emr.types.step_ids_list

        out["step_ids"] = aws_sdk_emr.types.step_ids_list.deserialize_aws_json_1_1(
            data["StepIds"]
        )
    if "StepCancellationOption" in data:
        import aws_sdk_emr.types.step_cancellation_option

        out["step_cancellation_option"] = (
            aws_sdk_emr.types.step_cancellation_option.deserialize_aws_json_1_1(
                data["StepCancellationOption"]
            )
        )
    return out

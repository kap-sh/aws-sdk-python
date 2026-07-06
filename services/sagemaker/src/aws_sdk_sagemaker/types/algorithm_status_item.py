"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmStatusItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.detailed_algorithm_status
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.string


class AlgorithmStatusItem(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the algorithm for which the overall status is being reported.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.detailed_algorithm_status.DetailedAlgorithmStatus"
    ]
    """<p>The current status.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>if the overall status is <code>Failed</code>, the reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmStatusItem) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_sagemaker.types.detailed_algorithm_status

        out["Status"] = (
            aws_sdk_sagemaker.types.detailed_algorithm_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmStatusItem:
    out: AlgorithmStatusItem = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.detailed_algorithm_status

        out["status"] = (
            aws_sdk_sagemaker.types.detailed_algorithm_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out

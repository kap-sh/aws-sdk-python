"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_arn
    import aws_sdk_sagemaker.types.algorithm_status
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.entity_name


class AlgorithmSummary(TypedDict):
    algorithm_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the algorithm that is described by the summary.</p>"""
    algorithm_arn: NotRequired["aws_sdk_sagemaker.types.algorithm_arn.AlgorithmArn"]
    """<p>The Amazon Resource Name (ARN) of the algorithm.</p>"""
    algorithm_description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A brief description of the algorithm.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that shows when the algorithm was created.</p>"""
    algorithm_status: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_status.AlgorithmStatus"
    ]
    """<p>The overall status of the algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmSummary) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "algorithm_arn" in value:
        out["AlgorithmArn"] = value["algorithm_arn"]
    if "algorithm_description" in value:
        out["AlgorithmDescription"] = value["algorithm_description"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "algorithm_status" in value:
        import aws_sdk_sagemaker.types.algorithm_status

        out["AlgorithmStatus"] = (
            aws_sdk_sagemaker.types.algorithm_status.serialize_aws_json_1_1(
                value["algorithm_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmSummary:
    out: AlgorithmSummary = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    if "AlgorithmArn" in data:
        out["algorithm_arn"] = data["AlgorithmArn"]
    if "AlgorithmDescription" in data:
        out["algorithm_description"] = data["AlgorithmDescription"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "AlgorithmStatus" in data:
        import aws_sdk_sagemaker.types.algorithm_status

        out["algorithm_status"] = (
            aws_sdk_sagemaker.types.algorithm_status.deserialize_aws_json_1_1(
                data["AlgorithmStatus"]
            )
        )
    return out

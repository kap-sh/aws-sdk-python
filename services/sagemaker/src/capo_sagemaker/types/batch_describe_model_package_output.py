"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDescribeModelPackageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_describe_model_package_error_map
    import capo_sagemaker.types.model_package_summaries


class BatchDescribeModelPackageOutput(TypedDict, closed=True):
    model_package_summaries: NotRequired[
        "capo_sagemaker.types.model_package_summaries.ModelPackageSummaries"
    ]
    """<p>The summaries for the model package versions</p>"""
    batch_describe_model_package_error_map: NotRequired[
        "capo_sagemaker.types.batch_describe_model_package_error_map.BatchDescribeModelPackageErrorMap"
    ]
    """<p>A map of the resource and BatchDescribeModelPackageError objects reporting the error associated with describing the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeModelPackageOutput) -> dict:
    out: dict = {}
    if "model_package_summaries" in value:
        import capo_sagemaker.types.model_package_summaries

        out["ModelPackageSummaries"] = (
            capo_sagemaker.types.model_package_summaries.serialize_aws_json_1_1(
                value["model_package_summaries"]
            )
        )
    if "batch_describe_model_package_error_map" in value:
        import capo_sagemaker.types.batch_describe_model_package_error_map

        out["BatchDescribeModelPackageErrorMap"] = (
            capo_sagemaker.types.batch_describe_model_package_error_map.serialize_aws_json_1_1(
                value["batch_describe_model_package_error_map"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeModelPackageOutput:
    out: BatchDescribeModelPackageOutput = {}  # type: ignore[typeddict-item]
    if "ModelPackageSummaries" in data:
        import capo_sagemaker.types.model_package_summaries

        out["model_package_summaries"] = (
            capo_sagemaker.types.model_package_summaries.deserialize_aws_json_1_1(
                data["ModelPackageSummaries"]
            )
        )
    if "BatchDescribeModelPackageErrorMap" in data:
        import capo_sagemaker.types.batch_describe_model_package_error_map

        out["batch_describe_model_package_error_map"] = (
            capo_sagemaker.types.batch_describe_model_package_error_map.deserialize_aws_json_1_1(
                data["BatchDescribeModelPackageErrorMap"]
            )
        )
    return out

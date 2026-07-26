"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageStatusItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.detailed_model_package_status
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.string


class ModelPackageStatusItem(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model package for which the overall status is being reported.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.detailed_model_package_status.DetailedModelPackageStatus"
    ]
    """<p>The current status.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.string.String"]
    """<p>if the overall status is <code>Failed</code>, the reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageStatusItem) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_sagemaker.types.detailed_model_package_status

        out["Status"] = (
            capo_sagemaker.types.detailed_model_package_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageStatusItem:
    out: ModelPackageStatusItem = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_sagemaker.types.detailed_model_package_status

        out["status"] = (
            capo_sagemaker.types.detailed_model_package_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out

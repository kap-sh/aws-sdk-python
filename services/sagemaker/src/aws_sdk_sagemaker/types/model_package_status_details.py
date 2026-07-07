"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_status_item_list


class ModelPackageStatusDetails(TypedDict, closed=True):
    validation_statuses: NotRequired[
        "aws_sdk_sagemaker.types.model_package_status_item_list.ModelPackageStatusItemList"
    ]
    """<p>The validation status of the model package.</p>"""
    image_scan_statuses: NotRequired[
        "aws_sdk_sagemaker.types.model_package_status_item_list.ModelPackageStatusItemList"
    ]
    """<p>The status of the scan of the Docker image container for the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageStatusDetails) -> dict:
    out: dict = {}
    if "validation_statuses" in value:
        import aws_sdk_sagemaker.types.model_package_status_item_list

        out["ValidationStatuses"] = (
            aws_sdk_sagemaker.types.model_package_status_item_list.serialize_aws_json_1_1(
                value["validation_statuses"]
            )
        )
    if "image_scan_statuses" in value:
        import aws_sdk_sagemaker.types.model_package_status_item_list

        out["ImageScanStatuses"] = (
            aws_sdk_sagemaker.types.model_package_status_item_list.serialize_aws_json_1_1(
                value["image_scan_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageStatusDetails:
    out: ModelPackageStatusDetails = {}  # type: ignore[typeddict-item]
    if "ValidationStatuses" in data:
        import aws_sdk_sagemaker.types.model_package_status_item_list

        out["validation_statuses"] = (
            aws_sdk_sagemaker.types.model_package_status_item_list.deserialize_aws_json_1_1(
                data["ValidationStatuses"]
            )
        )
    if "ImageScanStatuses" in data:
        import aws_sdk_sagemaker.types.model_package_status_item_list

        out["image_scan_statuses"] = (
            aws_sdk_sagemaker.types.model_package_status_item_list.deserialize_aws_json_1_1(
                data["ImageScanStatuses"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_status_item_list


class AlgorithmStatusDetails(TypedDict, closed=True):
    validation_statuses: NotRequired[
        "capo_sagemaker.types.algorithm_status_item_list.AlgorithmStatusItemList"
    ]
    """<p>The status of algorithm validation.</p>"""
    image_scan_statuses: NotRequired[
        "capo_sagemaker.types.algorithm_status_item_list.AlgorithmStatusItemList"
    ]
    """<p>The status of the scan of the algorithm's Docker image container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmStatusDetails) -> dict:
    out: dict = {}
    if "validation_statuses" in value:
        import capo_sagemaker.types.algorithm_status_item_list

        out["ValidationStatuses"] = (
            capo_sagemaker.types.algorithm_status_item_list.serialize_aws_json_1_1(
                value["validation_statuses"]
            )
        )
    if "image_scan_statuses" in value:
        import capo_sagemaker.types.algorithm_status_item_list

        out["ImageScanStatuses"] = (
            capo_sagemaker.types.algorithm_status_item_list.serialize_aws_json_1_1(
                value["image_scan_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmStatusDetails:
    out: AlgorithmStatusDetails = {}  # type: ignore[typeddict-item]
    if "ValidationStatuses" in data:
        import capo_sagemaker.types.algorithm_status_item_list

        out["validation_statuses"] = (
            capo_sagemaker.types.algorithm_status_item_list.deserialize_aws_json_1_1(
                data["ValidationStatuses"]
            )
        )
    if "ImageScanStatuses" in data:
        import capo_sagemaker.types.algorithm_status_item_list

        out["image_scan_statuses"] = (
            capo_sagemaker.types.algorithm_status_item_list.deserialize_aws_json_1_1(
                data["ImageScanStatuses"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#SensitiveDataResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.sensitive_data_detections_list


class SensitiveDataResult(TypedDict):
    category: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The category of sensitive data that was detected. For example, the category can indicate that the sensitive data involved credentials, financial information, or personal information.</p>"""
    detections: NotRequired[
        "aws_sdk_securityhub.types.sensitive_data_detections_list.SensitiveDataDetectionsList"
    ]
    """<p>The list of detected instances of sensitive data.</p>"""
    total_count: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The total number of occurrences of sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataResult) -> dict:
    out: dict = {}
    if "category" in value:
        out["Category"] = value["category"]
    if "detections" in value:
        import aws_sdk_securityhub.types.sensitive_data_detections_list

        out["Detections"] = (
            aws_sdk_securityhub.types.sensitive_data_detections_list.serialize_json(
                value["detections"]
            )
        )
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> SensitiveDataResult:
    out: SensitiveDataResult = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        out["category"] = data["Category"]
    if "Detections" in data:
        import aws_sdk_securityhub.types.sensitive_data_detections_list

        out["detections"] = (
            aws_sdk_securityhub.types.sensitive_data_detections_list.deserialize_json(
                data["Detections"]
            )
        )
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    return out

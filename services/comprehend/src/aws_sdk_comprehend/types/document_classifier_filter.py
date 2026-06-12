"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_arn_name
    import aws_sdk_comprehend.types.model_status
    import aws_sdk_comprehend.types.timestamp


class DocumentClassifierFilter(TypedDict):
    status: NotRequired["aws_sdk_comprehend.types.model_status.ModelStatus"]
    """<p>Filters the list of classifiers based on status.</p>"""
    document_classifier_name: NotRequired[
        "aws_sdk_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name that you assigned to the document classifier</p>"""
    submit_time_before: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of classifiers based on the time that the classifier was submitted for processing. Returns only classifiers submitted before the specified time. Classifiers are returned in ascending order, oldest to newest.</p>"""
    submit_time_after: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of classifiers based on the time that the classifier was submitted for processing. Returns only classifiers submitted after the specified time. Classifiers are returned in descending order, newest to oldest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_comprehend.types.model_status

        out["Status"] = aws_sdk_comprehend.types.model_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "document_classifier_name" in value:
        out["DocumentClassifierName"] = value["document_classifier_name"]
    if "submit_time_before" in value:
        import aws_sdk_comprehend.types.timestamp

        out["SubmitTimeBefore"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["submit_time_before"]
            )
        )
    if "submit_time_after" in value:
        import aws_sdk_comprehend.types.timestamp

        out["SubmitTimeAfter"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["submit_time_after"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassifierFilter:
    out: DocumentClassifierFilter = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_comprehend.types.model_status

        out["status"] = aws_sdk_comprehend.types.model_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "DocumentClassifierName" in data:
        out["document_classifier_name"] = data["DocumentClassifierName"]
    if "SubmitTimeBefore" in data:
        import aws_sdk_comprehend.types.timestamp

        out["submit_time_before"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeBefore"]
            )
        )
    if "SubmitTimeAfter" in data:
        import aws_sdk_comprehend.types.timestamp

        out["submit_time_after"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeAfter"]
            )
        )
    return out

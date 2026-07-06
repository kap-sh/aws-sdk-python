"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_arn_name
    import aws_sdk_comprehend.types.model_status
    import aws_sdk_comprehend.types.timestamp


class EntityRecognizerFilter(TypedDict, closed=True):
    status: NotRequired["aws_sdk_comprehend.types.model_status.ModelStatus"]
    """<p>The status of an entity recognizer.</p>"""
    recognizer_name: NotRequired[
        "aws_sdk_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name that you assigned the entity recognizer.</p>"""
    submit_time_before: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of entities based on the time that the list was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.</p>"""
    submit_time_after: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of entities based on the time that the list was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_comprehend.types.model_status

        out["Status"] = aws_sdk_comprehend.types.model_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "recognizer_name" in value:
        out["RecognizerName"] = value["recognizer_name"]
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


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerFilter:
    out: EntityRecognizerFilter = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_comprehend.types.model_status

        out["status"] = aws_sdk_comprehend.types.model_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "RecognizerName" in data:
        out["recognizer_name"] = data["RecognizerName"]
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

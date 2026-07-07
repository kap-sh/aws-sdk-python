"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Notifications``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.sns_topic


class Notifications(TypedDict, closed=True):
    progressing: NotRequired["aws_sdk_elastic_transcoder.types.sns_topic.SnsTopic"]
    """<p>The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.</p>"""
    completed: NotRequired["aws_sdk_elastic_transcoder.types.sns_topic.SnsTopic"]
    """<p>The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.</p>"""
    warning: NotRequired["aws_sdk_elastic_transcoder.types.sns_topic.SnsTopic"]
    """<p>The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.</p>"""
    error: NotRequired["aws_sdk_elastic_transcoder.types.sns_topic.SnsTopic"]
    """<p>The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Notifications) -> dict:
    out: dict = {}
    if "progressing" in value:
        out["Progressing"] = value["progressing"]
    if "completed" in value:
        out["Completed"] = value["completed"]
    if "warning" in value:
        out["Warning"] = value["warning"]
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_json(data: dict) -> Notifications:
    out: Notifications = {}  # type: ignore[typeddict-item]
    if "Progressing" in data:
        out["progressing"] = data["Progressing"]
    if "Completed" in data:
        out["completed"] = data["Completed"]
    if "Warning" in data:
        out["warning"] = data["Warning"]
    if "Error" in data:
        out["error"] = data["Error"]
    return out

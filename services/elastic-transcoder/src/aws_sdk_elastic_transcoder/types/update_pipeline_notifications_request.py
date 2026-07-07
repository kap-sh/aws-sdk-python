"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#UpdatePipelineNotificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_transcoder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id
    import aws_sdk_elastic_transcoder.types.notifications


class UpdatePipelineNotificationsRequest(TypedDict, closed=True):
    id: "aws_sdk_elastic_transcoder.types.id.Id"
    """<p>The identifier of the pipeline for which you want to change notification settings.</p>"""
    notifications: "aws_sdk_elastic_transcoder.types.notifications.Notifications"
    """<p>The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.</p> <important> <p>To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.</p> </important> <ul> <li> <p> <b>Progressing</b>: The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process jobs that are added to this pipeline. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Complete</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Warning</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> <li> <p> <b>Error</b>: The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition. This is the ARN that Amazon SNS returned when you created the topic.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipelineNotificationsRequest) -> dict:
    out: dict = {}
    import aws_sdk_elastic_transcoder.types.notifications

    out["Notifications"] = (
        aws_sdk_elastic_transcoder.types.notifications.serialize_json(
            value["notifications"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePipelineNotificationsRequest:
    out: UpdatePipelineNotificationsRequest = {}  # type: ignore[typeddict-item]
    if "Notifications" in data:
        import aws_sdk_elastic_transcoder.types.notifications

        out["notifications"] = (
            aws_sdk_elastic_transcoder.types.notifications.deserialize_json(
                data["Notifications"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePipelineNotificationsRequest.notifications required"
        )
    return out

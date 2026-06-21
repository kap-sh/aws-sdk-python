"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatOutputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qbusiness._iter import AnyIterator
from aws_sdk_qbusiness._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_review_event
    import aws_sdk_qbusiness.types.auth_challenge_request_event
    import aws_sdk_qbusiness.types.failed_attachment_event
    import aws_sdk_qbusiness.types.metadata_event
    import aws_sdk_qbusiness.types.text_output_event


class _ChatOutputStream_textEvent(TypedDict):
    textEvent: "aws_sdk_qbusiness.types.text_output_event.TextOutputEvent"


class _ChatOutputStream_metadataEvent(TypedDict):
    metadataEvent: "aws_sdk_qbusiness.types.metadata_event.MetadataEvent"


class _ChatOutputStream_actionReviewEvent(TypedDict):
    actionReviewEvent: "aws_sdk_qbusiness.types.action_review_event.ActionReviewEvent"


class _ChatOutputStream_failedAttachmentEvent(TypedDict):
    failedAttachmentEvent: (
        "aws_sdk_qbusiness.types.failed_attachment_event.FailedAttachmentEvent"
    )


class _ChatOutputStream_authChallengeRequestEvent(TypedDict):
    authChallengeRequestEvent: (
        "aws_sdk_qbusiness.types.auth_challenge_request_event.AuthChallengeRequestEvent"
    )


_ChatOutputStream: TypeAlias = (
    _ChatOutputStream_textEvent
    | _ChatOutputStream_metadataEvent
    | _ChatOutputStream_actionReviewEvent
    | _ChatOutputStream_failedAttachmentEvent
    | _ChatOutputStream_authChallengeRequestEvent
)
ChatOutputStream: TypeAlias = AnyIterator[_ChatOutputStream]


def serialize_event_json(value: _ChatOutputStream) -> bytes:
    match value:
        case {"textEvent": payload}:
            import aws_sdk_qbusiness.types.text_output_event

            return aws_sdk_qbusiness.types.text_output_event.serialize_event_json(
                payload
            )
        case {"metadataEvent": payload}:
            import aws_sdk_qbusiness.types.metadata_event

            return aws_sdk_qbusiness.types.metadata_event.serialize_event_json(payload)
        case {"actionReviewEvent": payload}:
            import aws_sdk_qbusiness.types.action_review_event

            return aws_sdk_qbusiness.types.action_review_event.serialize_event_json(
                payload
            )
        case {"failedAttachmentEvent": payload}:
            import aws_sdk_qbusiness.types.failed_attachment_event

            return aws_sdk_qbusiness.types.failed_attachment_event.serialize_event_json(
                payload
            )
        case {"authChallengeRequestEvent": payload}:
            import aws_sdk_qbusiness.types.auth_challenge_request_event

            return aws_sdk_qbusiness.types.auth_challenge_request_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ChatOutputStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ChatOutputStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "textEvent":
            import aws_sdk_qbusiness.types.text_output_event

            return {
                "textEvent": aws_sdk_qbusiness.types.text_output_event.deserialize_event_json(
                    message
                )
            }
        case "metadataEvent":
            import aws_sdk_qbusiness.types.metadata_event

            return {
                "metadataEvent": aws_sdk_qbusiness.types.metadata_event.deserialize_event_json(
                    message
                )
            }
        case "actionReviewEvent":
            import aws_sdk_qbusiness.types.action_review_event

            return {
                "actionReviewEvent": aws_sdk_qbusiness.types.action_review_event.deserialize_event_json(
                    message
                )
            }
        case "failedAttachmentEvent":
            import aws_sdk_qbusiness.types.failed_attachment_event

            return {
                "failedAttachmentEvent": aws_sdk_qbusiness.types.failed_attachment_event.deserialize_event_json(
                    message
                )
            }
        case "authChallengeRequestEvent":
            import aws_sdk_qbusiness.types.auth_challenge_request_event

            return {
                "authChallengeRequestEvent": aws_sdk_qbusiness.types.auth_challenge_request_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"ChatOutputStream: unrecognized event-type {event_type!r}"
            )

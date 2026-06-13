"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatOutputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, SerializationError

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


ChatOutputStream: TypeAlias = (
    _ChatOutputStream_textEvent
    | _ChatOutputStream_metadataEvent
    | _ChatOutputStream_actionReviewEvent
    | _ChatOutputStream_failedAttachmentEvent
    | _ChatOutputStream_authChallengeRequestEvent
)


# --- restJson1 ser/de ---
def serialize_json(value: ChatOutputStream) -> dict:
    if "textEvent" in value:
        import aws_sdk_qbusiness.types.text_output_event

        return {
            "textEvent": aws_sdk_qbusiness.types.text_output_event.serialize_json(
                value["textEvent"]
            )
        }
    elif "metadataEvent" in value:
        import aws_sdk_qbusiness.types.metadata_event

        return {
            "metadataEvent": aws_sdk_qbusiness.types.metadata_event.serialize_json(
                value["metadataEvent"]
            )
        }
    elif "actionReviewEvent" in value:
        import aws_sdk_qbusiness.types.action_review_event

        return {
            "actionReviewEvent": aws_sdk_qbusiness.types.action_review_event.serialize_json(
                value["actionReviewEvent"]
            )
        }
    elif "failedAttachmentEvent" in value:
        import aws_sdk_qbusiness.types.failed_attachment_event

        return {
            "failedAttachmentEvent": aws_sdk_qbusiness.types.failed_attachment_event.serialize_json(
                value["failedAttachmentEvent"]
            )
        }
    elif "authChallengeRequestEvent" in value:
        import aws_sdk_qbusiness.types.auth_challenge_request_event

        return {
            "authChallengeRequestEvent": aws_sdk_qbusiness.types.auth_challenge_request_event.serialize_json(
                value["authChallengeRequestEvent"]
            )
        }
    else:
        raise SerializationError("ChatOutputStream: no variant present")


def deserialize_json(data: dict) -> ChatOutputStream:
    if "textEvent" in data:
        import aws_sdk_qbusiness.types.text_output_event

        return {
            "textEvent": aws_sdk_qbusiness.types.text_output_event.deserialize_json(
                data["textEvent"]
            )
        }
    elif "metadataEvent" in data:
        import aws_sdk_qbusiness.types.metadata_event

        return {
            "metadataEvent": aws_sdk_qbusiness.types.metadata_event.deserialize_json(
                data["metadataEvent"]
            )
        }
    elif "actionReviewEvent" in data:
        import aws_sdk_qbusiness.types.action_review_event

        return {
            "actionReviewEvent": aws_sdk_qbusiness.types.action_review_event.deserialize_json(
                data["actionReviewEvent"]
            )
        }
    elif "failedAttachmentEvent" in data:
        import aws_sdk_qbusiness.types.failed_attachment_event

        return {
            "failedAttachmentEvent": aws_sdk_qbusiness.types.failed_attachment_event.deserialize_json(
                data["failedAttachmentEvent"]
            )
        }
    elif "authChallengeRequestEvent" in data:
        import aws_sdk_qbusiness.types.auth_challenge_request_event

        return {
            "authChallengeRequestEvent": aws_sdk_qbusiness.types.auth_challenge_request_event.deserialize_json(
                data["authChallengeRequestEvent"]
            )
        }
    else:
        raise DeserializationError("ChatOutputStream: no recognized variant key")

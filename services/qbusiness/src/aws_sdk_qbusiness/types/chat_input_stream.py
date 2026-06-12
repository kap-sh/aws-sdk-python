"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatInputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_execution_event
    import aws_sdk_qbusiness.types.end_of_input_event
    import aws_sdk_qbusiness.types.text_input_event
    import aws_sdk_qbusiness.types.auth_challenge_response_event
    import aws_sdk_qbusiness.types.configuration_event
    import aws_sdk_qbusiness.types.attachment_input_event

class _ChatInputStream_configurationEvent(TypedDict):
    configurationEvent: "aws_sdk_qbusiness.types.configuration_event.ConfigurationEvent"


class _ChatInputStream_textEvent(TypedDict):
    textEvent: "aws_sdk_qbusiness.types.text_input_event.TextInputEvent"


class _ChatInputStream_attachmentEvent(TypedDict):
    attachmentEvent: "aws_sdk_qbusiness.types.attachment_input_event.AttachmentInputEvent"


class _ChatInputStream_actionExecutionEvent(TypedDict):
    actionExecutionEvent: "aws_sdk_qbusiness.types.action_execution_event.ActionExecutionEvent"


class _ChatInputStream_endOfInputEvent(TypedDict):
    endOfInputEvent: "aws_sdk_qbusiness.types.end_of_input_event.EndOfInputEvent"


class _ChatInputStream_authChallengeResponseEvent(TypedDict):
    authChallengeResponseEvent: "aws_sdk_qbusiness.types.auth_challenge_response_event.AuthChallengeResponseEvent"

ChatInputStream: TypeAlias = _ChatInputStream_configurationEvent | _ChatInputStream_textEvent | _ChatInputStream_attachmentEvent | _ChatInputStream_actionExecutionEvent | _ChatInputStream_endOfInputEvent | _ChatInputStream_authChallengeResponseEvent

# --- restJson1 ser/de ---
def serialize_json(value: ChatInputStream) -> dict:
    if "configurationEvent" in value:
        import aws_sdk_qbusiness.types.configuration_event
        return {"configurationEvent": aws_sdk_qbusiness.types.configuration_event.serialize_json(value["configurationEvent"])}
    elif "textEvent" in value:
        import aws_sdk_qbusiness.types.text_input_event
        return {"textEvent": aws_sdk_qbusiness.types.text_input_event.serialize_json(value["textEvent"])}
    elif "attachmentEvent" in value:
        import aws_sdk_qbusiness.types.attachment_input_event
        return {"attachmentEvent": aws_sdk_qbusiness.types.attachment_input_event.serialize_json(value["attachmentEvent"])}
    elif "actionExecutionEvent" in value:
        import aws_sdk_qbusiness.types.action_execution_event
        return {"actionExecutionEvent": aws_sdk_qbusiness.types.action_execution_event.serialize_json(value["actionExecutionEvent"])}
    elif "endOfInputEvent" in value:
        import aws_sdk_qbusiness.types.end_of_input_event
        return {"endOfInputEvent": aws_sdk_qbusiness.types.end_of_input_event.serialize_json(value["endOfInputEvent"])}
    elif "authChallengeResponseEvent" in value:
        import aws_sdk_qbusiness.types.auth_challenge_response_event
        return {"authChallengeResponseEvent": aws_sdk_qbusiness.types.auth_challenge_response_event.serialize_json(value["authChallengeResponseEvent"])}
    else:
        raise SerializationError("ChatInputStream: no variant present")


def deserialize_json(data: dict) -> ChatInputStream:
    if "configurationEvent" in data:
        import aws_sdk_qbusiness.types.configuration_event
        return {"configurationEvent": aws_sdk_qbusiness.types.configuration_event.deserialize_json(data["configurationEvent"])}
    elif "textEvent" in data:
        import aws_sdk_qbusiness.types.text_input_event
        return {"textEvent": aws_sdk_qbusiness.types.text_input_event.deserialize_json(data["textEvent"])}
    elif "attachmentEvent" in data:
        import aws_sdk_qbusiness.types.attachment_input_event
        return {"attachmentEvent": aws_sdk_qbusiness.types.attachment_input_event.deserialize_json(data["attachmentEvent"])}
    elif "actionExecutionEvent" in data:
        import aws_sdk_qbusiness.types.action_execution_event
        return {"actionExecutionEvent": aws_sdk_qbusiness.types.action_execution_event.deserialize_json(data["actionExecutionEvent"])}
    elif "endOfInputEvent" in data:
        import aws_sdk_qbusiness.types.end_of_input_event
        return {"endOfInputEvent": aws_sdk_qbusiness.types.end_of_input_event.deserialize_json(data["endOfInputEvent"])}
    elif "authChallengeResponseEvent" in data:
        import aws_sdk_qbusiness.types.auth_challenge_response_event
        return {"authChallengeResponseEvent": aws_sdk_qbusiness.types.auth_challenge_response_event.deserialize_json(data["authChallengeResponseEvent"])}
    else:
        raise DeserializationError("ChatInputStream: no recognized variant key")
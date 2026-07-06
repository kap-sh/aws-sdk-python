"""Generated from Smithy shape ``com.amazonaws.qbusiness#TopicConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.example_chat_messages
    import aws_sdk_qbusiness.types.rules
    import aws_sdk_qbusiness.types.topic_configuration_name
    import aws_sdk_qbusiness.types.topic_description


class TopicConfiguration(TypedDict, closed=True):
    name: "aws_sdk_qbusiness.types.topic_configuration_name.TopicConfigurationName"
    """<p>A name for your topic control configuration.</p>"""
    description: NotRequired[
        "aws_sdk_qbusiness.types.topic_description.TopicDescription"
    ]
    """<p>A description for your topic control configuration. Use this to outline how the large language model (LLM) should use this topic control configuration.</p>"""
    example_chat_messages: NotRequired[
        "aws_sdk_qbusiness.types.example_chat_messages.ExampleChatMessages"
    ]
    """<p>A list of example phrases that you expect the end user to use in relation to the topic.</p>"""
    rules: "aws_sdk_qbusiness.types.rules.Rules"
    """<p>Rules defined for a topic configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "example_chat_messages" in value:
        import aws_sdk_qbusiness.types.example_chat_messages

        out["exampleChatMessages"] = (
            aws_sdk_qbusiness.types.example_chat_messages.serialize_json(
                value["example_chat_messages"]
            )
        )
    import aws_sdk_qbusiness.types.rules

    out["rules"] = aws_sdk_qbusiness.types.rules.serialize_json(value["rules"])
    return out


def deserialize_json(data: dict) -> TopicConfiguration:
    out: TopicConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TopicConfiguration.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "exampleChatMessages" in data:
        import aws_sdk_qbusiness.types.example_chat_messages

        out["example_chat_messages"] = (
            aws_sdk_qbusiness.types.example_chat_messages.deserialize_json(
                data["exampleChatMessages"]
            )
        )
    if "rules" in data:
        import aws_sdk_qbusiness.types.rules

        out["rules"] = aws_sdk_qbusiness.types.rules.deserialize_json(data["rules"])
    else:
        raise DeserializationError("TopicConfiguration.rules required")
    return out

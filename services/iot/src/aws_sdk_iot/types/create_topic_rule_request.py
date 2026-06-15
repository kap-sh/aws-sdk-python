"""Generated from Smithy shape ``com.amazonaws.iot#CreateTopicRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.rule_name
    import aws_sdk_iot.types.string
    import aws_sdk_iot.types.topic_rule_payload


class CreateTopicRuleRequest(TypedDict):
    rule_name: "aws_sdk_iot.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    topic_rule_payload: "aws_sdk_iot.types.topic_rule_payload.TopicRulePayload"
    """<p>The rule payload.</p>"""
    tags: NotRequired["aws_sdk_iot.types.string.String"]
    r"""<p>Metadata which can be used to manage the topic rule.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: --tags \"key1=value1&key2=value2...\"</p> <p>For the cli-input-json file use format: \"tags\": \"key1=value1&key2=value2...\"</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.topic_rule_payload

    out["topicRulePayload"] = aws_sdk_iot.types.topic_rule_payload.serialize_json(
        value["topic_rule_payload"]
    )
    return out


def deserialize_json(data: dict) -> CreateTopicRuleRequest:
    out: CreateTopicRuleRequest = {}  # type: ignore[typeddict-item]
    if "topicRulePayload" in data:
        import aws_sdk_iot.types.topic_rule_payload

        out["topic_rule_payload"] = (
            aws_sdk_iot.types.topic_rule_payload.deserialize_json(
                data["topicRulePayload"]
            )
        )
    else:
        raise DeserializationError("CreateTopicRuleRequest.topic_rule_payload required")
    return out

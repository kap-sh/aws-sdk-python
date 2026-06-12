"""Generated from Smithy shape ``com.amazonaws.iot#CreateTopicRuleDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.topic_rule_destination_configuration


class CreateTopicRuleDestinationRequest(TypedDict):
    destination_configuration: "aws_sdk_iot.types.topic_rule_destination_configuration.TopicRuleDestinationConfiguration"
    """<p>The topic rule destination configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicRuleDestinationRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.topic_rule_destination_configuration

    out["destinationConfiguration"] = (
        aws_sdk_iot.types.topic_rule_destination_configuration.serialize_json(
            value["destination_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateTopicRuleDestinationRequest:
    out: CreateTopicRuleDestinationRequest = {}  # type: ignore[typeddict-item]
    if "destinationConfiguration" in data:
        import aws_sdk_iot.types.topic_rule_destination_configuration

        out["destination_configuration"] = (
            aws_sdk_iot.types.topic_rule_destination_configuration.deserialize_json(
                data["destinationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTopicRuleDestinationRequest.destination_configuration required"
        )
    return out

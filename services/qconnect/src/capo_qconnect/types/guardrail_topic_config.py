"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailTopicConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_topic_definition
    import capo_qconnect.types.guardrail_topic_examples
    import capo_qconnect.types.guardrail_topic_name
    import capo_qconnect.types.guardrail_topic_type


class GuardrailTopicConfig(TypedDict, closed=True):
    name: "capo_qconnect.types.guardrail_topic_name.GuardrailTopicName"
    """<p>The name of the topic to deny.</p>"""
    definition: (
        "capo_qconnect.types.guardrail_topic_definition.GuardrailTopicDefinition"
    )
    """<p>A definition of the topic to deny.</p>"""
    examples: NotRequired[
        "capo_qconnect.types.guardrail_topic_examples.GuardrailTopicExamples"
    ]
    """<p>A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.</p>"""
    type: "capo_qconnect.types.guardrail_topic_type.GuardrailTopicType"
    """<p>Specifies to deny the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicConfig) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["definition"] = value["definition"]
    if "examples" in value:
        import capo_qconnect.types.guardrail_topic_examples

        out["examples"] = capo_qconnect.types.guardrail_topic_examples.serialize_json(
            value["examples"]
        )
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> GuardrailTopicConfig:
    out: GuardrailTopicConfig = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GuardrailTopicConfig.name required")
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("GuardrailTopicConfig.definition required")
    if "examples" in data:
        import capo_qconnect.types.guardrail_topic_examples

        out["examples"] = capo_qconnect.types.guardrail_topic_examples.deserialize_json(
            data["examples"]
        )
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GuardrailTopicConfig.type required")
    return out

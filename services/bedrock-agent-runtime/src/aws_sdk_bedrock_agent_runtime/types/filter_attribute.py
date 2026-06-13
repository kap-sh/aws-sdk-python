"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FilterAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.filter_key
    import aws_sdk_bedrock_agent_runtime.types.filter_value


class FilterAttribute(TypedDict):
    key: "aws_sdk_bedrock_agent_runtime.types.filter_key.FilterKey"
    """<p>The name that the metadata attribute must match.</p>"""
    value: "aws_sdk_bedrock_agent_runtime.types.filter_value.FilterValue"
    """<p>The value to whcih to compare the value of the metadata attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> FilterAttribute:
    out: FilterAttribute = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("FilterAttribute.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("FilterAttribute.value required")
    return out

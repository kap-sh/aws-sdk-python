"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Filter``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.filter_operator
    import aws_sdk_bedrock_agentcore_control.types.filter_value

class Filter(TypedDict):
    key: "str"
    """<p> The key or field name to filter on within the agent trace data. </p>"""
    operator: "aws_sdk_bedrock_agentcore_control.types.filter_operator.FilterOperator"
    """<p> The comparison operator to use for filtering. </p>"""
    value: "aws_sdk_bedrock_agentcore_control.types.filter_value.FilterValue"
    """<p> The value to compare against using the specified operator. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_bedrock_agentcore_control.types.filter_operator
    out["operator"] = aws_sdk_bedrock_agentcore_control.types.filter_operator.serialize_json(value["operator"])
    import aws_sdk_bedrock_agentcore_control.types.filter_value
    out["value"] = aws_sdk_bedrock_agentcore_control.types.filter_value.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Filter.key required")
    if "operator" in data:
        import aws_sdk_bedrock_agentcore_control.types.filter_operator
        out["operator"] = aws_sdk_bedrock_agentcore_control.types.filter_operator.deserialize_json(data["operator"])
    else:
        raise DeserializationError("Filter.operator required")
    if "value" in data:
        import aws_sdk_bedrock_agentcore_control.types.filter_value
        out["value"] = aws_sdk_bedrock_agentcore_control.types.filter_value.deserialize_json(data["value"])
    else:
        raise DeserializationError("Filter.value required")
    return out
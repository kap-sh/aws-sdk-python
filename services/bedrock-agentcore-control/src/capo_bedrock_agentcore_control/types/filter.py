"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.filter_operator
    import capo_bedrock_agentcore_control.types.filter_value


class Filter(TypedDict, closed=True):
    key: "str"
    """<p> The key or field name to filter on within the agent trace data. </p>"""
    operator: "capo_bedrock_agentcore_control.types.filter_operator.FilterOperator"
    """<p> The comparison operator to use for filtering. </p>"""
    value: "capo_bedrock_agentcore_control.types.filter_value.FilterValue"
    """<p> The value to compare against using the specified operator. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock_agentcore_control.types.filter_operator

    out["operator"] = (
        capo_bedrock_agentcore_control.types.filter_operator.serialize_json(
            value["operator"]
        )
    )
    import capo_bedrock_agentcore_control.types.filter_value

    out["value"] = capo_bedrock_agentcore_control.types.filter_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Filter.key required")
    if "operator" in data:
        import capo_bedrock_agentcore_control.types.filter_operator

        out["operator"] = (
            capo_bedrock_agentcore_control.types.filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("Filter.operator required")
    if "value" in data:
        import capo_bedrock_agentcore_control.types.filter_value

        out["value"] = (
            capo_bedrock_agentcore_control.types.filter_value.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("Filter.value required")
    return out

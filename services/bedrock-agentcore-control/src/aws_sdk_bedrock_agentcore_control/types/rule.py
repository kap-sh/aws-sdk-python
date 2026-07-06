"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.filter_list
    import aws_sdk_bedrock_agentcore_control.types.sampling_config
    import aws_sdk_bedrock_agentcore_control.types.session_config


class Rule(TypedDict, closed=True):
    sampling_config: (
        "aws_sdk_bedrock_agentcore_control.types.sampling_config.SamplingConfig"
    )
    """<p> The sampling configuration that determines what percentage of agent traces to evaluate. </p>"""
    filters: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.filter_list.FilterList"
    ]
    """<p> The list of filters that determine which agent traces should be included in the evaluation based on trace properties. </p>"""
    session_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.session_config.SessionConfig"
    ]
    """<p> The session configuration that defines timeout settings for detecting when agent sessions are complete and ready for evaluation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.sampling_config

    out["samplingConfig"] = (
        aws_sdk_bedrock_agentcore_control.types.sampling_config.serialize_json(
            value["sampling_config"]
        )
    )
    if "filters" in value:
        import aws_sdk_bedrock_agentcore_control.types.filter_list

        out["filters"] = (
            aws_sdk_bedrock_agentcore_control.types.filter_list.serialize_json(
                value["filters"]
            )
        )
    if "session_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.session_config

        out["sessionConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.session_config.serialize_json(
                value["session_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "samplingConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.sampling_config

        out["sampling_config"] = (
            aws_sdk_bedrock_agentcore_control.types.sampling_config.deserialize_json(
                data["samplingConfig"]
            )
        )
    else:
        raise DeserializationError("Rule.sampling_config required")
    if "filters" in data:
        import aws_sdk_bedrock_agentcore_control.types.filter_list

        out["filters"] = (
            aws_sdk_bedrock_agentcore_control.types.filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "sessionConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.session_config

        out["session_config"] = (
            aws_sdk_bedrock_agentcore_control.types.session_config.deserialize_json(
                data["sessionConfig"]
            )
        )
    return out

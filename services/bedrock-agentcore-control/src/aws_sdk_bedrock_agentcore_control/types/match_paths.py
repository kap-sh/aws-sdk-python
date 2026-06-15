"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPaths``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.match_path_patterns


class MatchPaths(TypedDict):
    any_of: (
        "aws_sdk_bedrock_agentcore_control.types.match_path_patterns.MatchPathPatterns"
    )
    """<p>A list of path patterns. The condition is met if the request path matches any of the patterns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchPaths) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.match_path_patterns

    out["anyOf"] = (
        aws_sdk_bedrock_agentcore_control.types.match_path_patterns.serialize_json(
            value["any_of"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatchPaths:
    out: MatchPaths = {}  # type: ignore[typeddict-item]
    if "anyOf" in data:
        import aws_sdk_bedrock_agentcore_control.types.match_path_patterns

        out["any_of"] = (
            aws_sdk_bedrock_agentcore_control.types.match_path_patterns.deserialize_json(
                data["anyOf"]
            )
        )
    else:
        raise DeserializationError("MatchPaths.any_of required")
    return out

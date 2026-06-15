"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPrincipals``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.match_principal_entries


class MatchPrincipals(TypedDict):
    any_of: "aws_sdk_bedrock_agentcore_control.types.match_principal_entries.MatchPrincipalEntries"
    """<p>A list of principal entries. The condition is met if any of the entries match the caller's identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchPrincipals) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.match_principal_entries

    out["anyOf"] = (
        aws_sdk_bedrock_agentcore_control.types.match_principal_entries.serialize_json(
            value["any_of"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatchPrincipals:
    out: MatchPrincipals = {}  # type: ignore[typeddict-item]
    if "anyOf" in data:
        import aws_sdk_bedrock_agentcore_control.types.match_principal_entries

        out["any_of"] = (
            aws_sdk_bedrock_agentcore_control.types.match_principal_entries.deserialize_json(
                data["anyOf"]
            )
        )
    else:
        raise DeserializationError("MatchPrincipals.any_of required")
    return out

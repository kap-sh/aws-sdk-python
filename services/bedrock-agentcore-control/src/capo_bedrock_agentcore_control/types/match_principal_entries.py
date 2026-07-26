"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPrincipalEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_principal_entry

MatchPrincipalEntries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.match_principal_entry.MatchPrincipalEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchPrincipalEntries) -> list:
    import capo_bedrock_agentcore_control.types.match_principal_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.match_principal_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MatchPrincipalEntries:
    import capo_bedrock_agentcore_control.types.match_principal_entry

    out: MatchPrincipalEntries = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.match_principal_entry.deserialize_json(
                item
            )
        )
    return out

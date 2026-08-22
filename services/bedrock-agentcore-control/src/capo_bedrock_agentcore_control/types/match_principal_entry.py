"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPrincipalEntry``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.iam_principal


class _MatchPrincipalEntry_iamPrincipal(TypedDict, closed=True):
    iamPrincipal: "capo_bedrock_agentcore_control.types.iam_principal.IamPrincipal"


MatchPrincipalEntry: TypeAlias = _MatchPrincipalEntry_iamPrincipal


# --- restJson1 ser/de ---
def serialize_json(value: MatchPrincipalEntry) -> dict:
    if "iamPrincipal" in value:
        import capo_bedrock_agentcore_control.types.iam_principal

        return {
            "iamPrincipal": capo_bedrock_agentcore_control.types.iam_principal.serialize_json(
                value["iamPrincipal"]
            )
        }
    else:
        raise SerializationError("MatchPrincipalEntry: no variant present")


def deserialize_json(data: dict) -> MatchPrincipalEntry:
    if data.get("iamPrincipal") is not None:
        import capo_bedrock_agentcore_control.types.iam_principal

        return {
            "iamPrincipal": capo_bedrock_agentcore_control.types.iam_principal.deserialize_json(
                data["iamPrincipal"]
            )
        }
    else:
        raise DeserializationError("MatchPrincipalEntry: no recognized variant key")

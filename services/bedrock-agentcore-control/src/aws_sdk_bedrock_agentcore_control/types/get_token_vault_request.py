"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetTokenVaultRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.token_vault_id_type


class GetTokenVaultRequest(TypedDict):
    token_vault_id: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
    ]
    """<p>The unique identifier of the token vault to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenVaultRequest) -> dict:
    out: dict = {}
    if "token_vault_id" in value:
        out["tokenVaultId"] = value["token_vault_id"]
    return out


def deserialize_json(data: dict) -> GetTokenVaultRequest:
    out: GetTokenVaultRequest = {}  # type: ignore[typeddict-item]
    if "tokenVaultId" in data:
        out["token_vault_id"] = data["tokenVaultId"]
    return out

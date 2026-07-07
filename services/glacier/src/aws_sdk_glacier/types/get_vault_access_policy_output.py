"""Generated from Smithy shape ``com.amazonaws.glacier#GetVaultAccessPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.vault_access_policy


class GetVaultAccessPolicyOutput(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_glacier.types.vault_access_policy.VaultAccessPolicy"]
    """<p>Contains the returned vault access policy as a JSON string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVaultAccessPolicyOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_glacier.types.vault_access_policy

        out["policy"] = aws_sdk_glacier.types.vault_access_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> GetVaultAccessPolicyOutput:
    out: GetVaultAccessPolicyOutput = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import aws_sdk_glacier.types.vault_access_policy

        out["policy"] = aws_sdk_glacier.types.vault_access_policy.deserialize_json(
            data["policy"]
        )
    return out

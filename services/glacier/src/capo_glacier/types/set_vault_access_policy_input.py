"""Generated from Smithy shape ``com.amazonaws.glacier#SetVaultAccessPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string
    import capo_glacier.types.vault_access_policy


class SetVaultAccessPolicyInput(TypedDict, closed=True):
    account_id: "capo_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "capo_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    policy: NotRequired["capo_glacier.types.vault_access_policy.VaultAccessPolicy"]
    """<p>The vault access policy as a JSON string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetVaultAccessPolicyInput) -> dict:
    out: dict = {}
    if "policy" in value:
        import capo_glacier.types.vault_access_policy

        out["policy"] = capo_glacier.types.vault_access_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> SetVaultAccessPolicyInput:
    out: SetVaultAccessPolicyInput = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        import capo_glacier.types.vault_access_policy

        out["policy"] = capo_glacier.types.vault_access_policy.deserialize_json(
            data["policy"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyStoreAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.alias
    import aws_sdk_verifiedpermissions.types.policy_store_id


class CreatePolicyStoreAliasInput(TypedDict):
    alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias"
    """<p>Specifies the name of the policy store alias to create. The name must be unique within your Amazon Web Services account and Amazon Web Services Region.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>"""
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store to associate with the alias.</p> <note> <p>The associated policy store must be specified using its ID. The alias name cannot be used.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyStoreAliasInput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    out["policyStoreId"] = value["policy_store_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyStoreAliasInput:
    out: CreatePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
    if "aliasName" in data:
        out["alias_name"] = data["aliasName"]
    else:
        raise DeserializationError("CreatePolicyStoreAliasInput.alias_name required")
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError(
            "CreatePolicyStoreAliasInput.policy_store_id required"
        )
    return out

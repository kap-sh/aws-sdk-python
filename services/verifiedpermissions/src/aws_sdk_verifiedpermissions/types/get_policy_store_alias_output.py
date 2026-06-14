"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyStoreAliasOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.alias
    import aws_sdk_verifiedpermissions.types.alias_state
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.resource_arn
    import aws_sdk_verifiedpermissions.types.timestamp_format


class GetPolicyStoreAliasOutput(TypedDict):
    alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias"
    """<p>The name of the policy store alias.</p>"""
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store associated with the alias.</p>"""
    alias_arn: "aws_sdk_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the policy store alias.</p>"""
    created_at: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy store alias was created.</p>"""
    state: "aws_sdk_verifiedpermissions.types.alias_state.AliasState"
    """<p>The state of the policy store alias. Policy Store Aliases in the Active state can be used normally. When a policy store alias is deleted, it enters the PendingDeletion state. Policy Store Aliases in the PendingDeletion cannot be used, and creating a policy store alias with the same alias name will fail.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyStoreAliasOutput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    out["policyStoreId"] = value["policy_store_id"]
    out["aliasArn"] = value["alias_arn"]
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["createdAt"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import aws_sdk_verifiedpermissions.types.alias_state

    out["state"] = aws_sdk_verifiedpermissions.types.alias_state.serialize_aws_json_1_0(
        value["state"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyStoreAliasOutput:
    out: GetPolicyStoreAliasOutput = {}  # type: ignore[typeddict-item]
    if "aliasName" in data:
        out["alias_name"] = data["aliasName"]
    else:
        raise DeserializationError("GetPolicyStoreAliasOutput.alias_name required")
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetPolicyStoreAliasOutput.policy_store_id required")
    if "aliasArn" in data:
        out["alias_arn"] = data["aliasArn"]
    else:
        raise DeserializationError("GetPolicyStoreAliasOutput.alias_arn required")
    if "createdAt" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_at"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetPolicyStoreAliasOutput.created_at required")
    if "state" in data:
        import aws_sdk_verifiedpermissions.types.alias_state

        out["state"] = (
            aws_sdk_verifiedpermissions.types.alias_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        raise DeserializationError("GetPolicyStoreAliasOutput.state required")
    return out

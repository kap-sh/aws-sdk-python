"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyStoreAliasOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_verifiedpermissions.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.alias
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.resource_arn
    import aws_sdk_verifiedpermissions.types.timestamp_format

class CreatePolicyStoreAliasOutput(TypedDict):
    alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias"
    """<p>The name of the policy store alias.</p>"""
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store associated with the alias.</p>"""
    alias_arn: "aws_sdk_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the policy store alias.</p>"""
    created_at: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy store alias was created.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyStoreAliasOutput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    out["policyStoreId"] = value["policy_store_id"]
    out["aliasArn"] = value["alias_arn"]
    import aws_sdk_verifiedpermissions.types.timestamp_format
    out["createdAt"] = aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(value["created_at"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyStoreAliasOutput:
    out: CreatePolicyStoreAliasOutput = {}  # type: ignore[typeddict-item]
    if "aliasName" in data:
        out["alias_name"] = data["aliasName"]
    else:
        raise DeserializationError("CreatePolicyStoreAliasOutput.alias_name required")
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("CreatePolicyStoreAliasOutput.policy_store_id required")
    if "aliasArn" in data:
        out["alias_arn"] = data["aliasArn"]
    else:
        raise DeserializationError("CreatePolicyStoreAliasOutput.alias_arn required")
    if "createdAt" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format
        out["created_at"] = aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(data["createdAt"])
    else:
        raise DeserializationError("CreatePolicyStoreAliasOutput.created_at required")
    return out
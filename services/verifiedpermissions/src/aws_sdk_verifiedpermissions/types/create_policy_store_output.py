"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyStoreOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_verifiedpermissions.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.resource_arn
    import aws_sdk_verifiedpermissions.types.timestamp_format

class CreatePolicyStoreOutput(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The unique ID of the new policy store.</p>"""
    arn: "aws_sdk_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the new policy store.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy store was originally created.</p>"""
    last_updated_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy store was last updated.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyStoreOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["arn"] = value["arn"]
    import aws_sdk_verifiedpermissions.types.timestamp_format
    out["createdDate"] = aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(value["created_date"])
    import aws_sdk_verifiedpermissions.types.timestamp_format
    out["lastUpdatedDate"] = aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(value["last_updated_date"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyStoreOutput:
    out: CreatePolicyStoreOutput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("CreatePolicyStoreOutput.policy_store_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreatePolicyStoreOutput.arn required")
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format
        out["created_date"] = aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(data["createdDate"])
    else:
        raise DeserializationError("CreatePolicyStoreOutput.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format
        out["last_updated_date"] = aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(data["lastUpdatedDate"])
    else:
        raise DeserializationError("CreatePolicyStoreOutput.last_updated_date required")
    return out
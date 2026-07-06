"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyStoreItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_description
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.resource_arn
    import aws_sdk_verifiedpermissions.types.timestamp_format


class PolicyStoreItem(TypedDict, closed=True):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The unique identifier of the policy store.</p>"""
    arn: "aws_sdk_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the policy store.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy was created.</p>"""
    last_updated_date: NotRequired[
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    ]
    """<p>The date and time the policy store was most recently updated.</p>"""
    description: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
    ]
    """<p>Descriptive text that you can provide to help with identification of the current policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStoreItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["arn"] = value["arn"]
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    if "last_updated_date" in value:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["lastUpdatedDate"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
                value["last_updated_date"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyStoreItem:
    out: PolicyStoreItem = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("PolicyStoreItem.policy_store_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("PolicyStoreItem.arn required")
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("PolicyStoreItem.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyOutputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_definition_detail
    import aws_sdk_verifiedpermissions.types.policy_id
    import aws_sdk_verifiedpermissions.types.policy_name
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.policy_type
    import aws_sdk_verifiedpermissions.types.timestamp_format


class BatchGetPolicyOutputItem(TypedDict, closed=True):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The identifier of the policy store where the policy you want information about is stored.</p>"""
    policy_id: "aws_sdk_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The identifier of the policy you want information about.</p>"""
    policy_type: "aws_sdk_verifiedpermissions.types.policy_type.PolicyType"
    """<p>The type of the policy. This is one of the following values:</p> <ul> <li> <p> <code>STATIC</code> </p> </li> <li> <p> <code>TEMPLATE_LINKED</code> </p> </li> </ul>"""
    definition: "aws_sdk_verifiedpermissions.types.policy_definition_detail.PolicyDefinitionDetail"
    """<p>The policy definition of an item in the list of policies returned.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy was created.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time the policy was most recently updated.</p>"""
    name: NotRequired["aws_sdk_verifiedpermissions.types.policy_name.PolicyName"]
    """<p>The name of the policy, if one was assigned when the policy was created or last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyOutputItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    import aws_sdk_verifiedpermissions.types.policy_type

    out["policyType"] = (
        aws_sdk_verifiedpermissions.types.policy_type.serialize_aws_json_1_0(
            value["policy_type"]
        )
    )
    import aws_sdk_verifiedpermissions.types.policy_definition_detail

    out["definition"] = (
        aws_sdk_verifiedpermissions.types.policy_definition_detail.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyOutputItem:
    out: BatchGetPolicyOutputItem = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("BatchGetPolicyOutputItem.policy_store_id required")
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("BatchGetPolicyOutputItem.policy_id required")
    if "policyType" in data:
        import aws_sdk_verifiedpermissions.types.policy_type

        out["policy_type"] = (
            aws_sdk_verifiedpermissions.types.policy_type.deserialize_aws_json_1_0(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError("BatchGetPolicyOutputItem.policy_type required")
    if "definition" in data:
        import aws_sdk_verifiedpermissions.types.policy_definition_detail

        out["definition"] = (
            aws_sdk_verifiedpermissions.types.policy_definition_detail.deserialize_aws_json_1_0(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("BatchGetPolicyOutputItem.definition required")
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("BatchGetPolicyOutputItem.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetPolicyOutputItem.last_updated_date required"
        )
    if "name" in data:
        out["name"] = data["name"]
    return out

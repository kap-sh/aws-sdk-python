"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.policy_template_id
    import aws_sdk_verifiedpermissions.types.timestamp_format


class CreatePolicyTemplateOutput(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the policy template.</p>"""
    policy_template_id: (
        "aws_sdk_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    )
    """<p>The unique ID of the new policy template.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy template was originally created.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time the policy template was most recently updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyTemplateOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyTemplateId"] = value["policy_template_id"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyTemplateOutput:
    out: CreatePolicyTemplateOutput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError(
            "CreatePolicyTemplateOutput.policy_store_id required"
        )
    if "policyTemplateId" in data:
        out["policy_template_id"] = data["policyTemplateId"]
    else:
        raise DeserializationError(
            "CreatePolicyTemplateOutput.policy_template_id required"
        )
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyTemplateOutput.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePolicyTemplateOutput.last_updated_date required"
        )
    return out

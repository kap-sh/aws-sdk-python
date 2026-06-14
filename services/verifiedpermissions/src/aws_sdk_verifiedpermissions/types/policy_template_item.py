"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyTemplateItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.policy_template_description
    import aws_sdk_verifiedpermissions.types.policy_template_id
    import aws_sdk_verifiedpermissions.types.policy_template_name
    import aws_sdk_verifiedpermissions.types.timestamp_format


class PolicyTemplateItem(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The unique identifier of the policy store that contains the template.</p>"""
    policy_template_id: (
        "aws_sdk_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    )
    """<p>The unique identifier of the policy template.</p>"""
    description: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_template_description.PolicyTemplateDescription"
    ]
    """<p>The description attached to the policy template.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy template was created.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time that the policy template was most recently updated.</p>"""
    name: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_template_name.PolicyTemplateName"
    ]
    """<p>The name of the policy template, if one was assigned when the policy template was created or last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyTemplateItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyTemplateId"] = value["policy_template_id"]
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_aws_json_1_0(data: dict) -> PolicyTemplateItem:
    out: PolicyTemplateItem = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("PolicyTemplateItem.policy_store_id required")
    if "policyTemplateId" in data:
        out["policy_template_id"] = data["policyTemplateId"]
    else:
        raise DeserializationError("PolicyTemplateItem.policy_template_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("PolicyTemplateItem.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("PolicyTemplateItem.last_updated_date required")
    if "name" in data:
        out["name"] = data["name"]
    return out

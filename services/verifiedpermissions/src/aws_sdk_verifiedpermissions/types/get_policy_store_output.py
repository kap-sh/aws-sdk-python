"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyStoreOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.cedar_version
    import aws_sdk_verifiedpermissions.types.deletion_protection
    import aws_sdk_verifiedpermissions.types.encryption_state
    import aws_sdk_verifiedpermissions.types.policy_store_description
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.resource_arn
    import aws_sdk_verifiedpermissions.types.tag_map
    import aws_sdk_verifiedpermissions.types.timestamp_format
    import aws_sdk_verifiedpermissions.types.validation_settings


class GetPolicyStoreOutput(TypedDict, closed=True):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store;</p>"""
    arn: "aws_sdk_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the policy store.</p>"""
    validation_settings: (
        "aws_sdk_verifiedpermissions.types.validation_settings.ValidationSettings"
    )
    """<p>The current validation settings for the policy store.</p>"""
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy store was originally created.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time that the policy store was last updated.</p>"""
    description: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
    ]
    """<p>Descriptive text that you can provide to help with identification of the current policy store.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_verifiedpermissions.types.deletion_protection.DeletionProtection"
    ]
    """<p>Specifies whether the policy store can be deleted. If enabled, the policy store can't be deleted.</p> <p>The default state is <code>DISABLED</code>.</p>"""
    encryption_state: NotRequired[
        "aws_sdk_verifiedpermissions.types.encryption_state.EncryptionState"
    ]
    """<p>A structure that contains the encryption configuration for the policy store.</p>"""
    cedar_version: NotRequired[
        "aws_sdk_verifiedpermissions.types.cedar_version.CedarVersion"
    ]
    r"""<p>The version of the Cedar language used with policies, policy templates, and schemas in this policy store. For more information, see <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/cedar4-faq.html\">Amazon Verified Permissions upgrade to Cedar v4 FAQ</a>.</p>"""
    tags: NotRequired["aws_sdk_verifiedpermissions.types.tag_map.TagMap"]
    """<p>The list of tags associated with the policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyStoreOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["arn"] = value["arn"]
    import aws_sdk_verifiedpermissions.types.validation_settings

    out["validationSettings"] = (
        aws_sdk_verifiedpermissions.types.validation_settings.serialize_aws_json_1_0(
            value["validation_settings"]
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
    if "description" in value:
        out["description"] = value["description"]
    if "deletion_protection" in value:
        import aws_sdk_verifiedpermissions.types.deletion_protection

        out["deletionProtection"] = (
            aws_sdk_verifiedpermissions.types.deletion_protection.serialize_aws_json_1_0(
                value["deletion_protection"]
            )
        )
    if "encryption_state" in value:
        import aws_sdk_verifiedpermissions.types.encryption_state

        out["encryptionState"] = (
            aws_sdk_verifiedpermissions.types.encryption_state.serialize_aws_json_1_0(
                value["encryption_state"]
            )
        )
    if "cedar_version" in value:
        import aws_sdk_verifiedpermissions.types.cedar_version

        out["cedarVersion"] = (
            aws_sdk_verifiedpermissions.types.cedar_version.serialize_aws_json_1_0(
                value["cedar_version"]
            )
        )
    if "tags" in value:
        import aws_sdk_verifiedpermissions.types.tag_map

        out["tags"] = aws_sdk_verifiedpermissions.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyStoreOutput:
    out: GetPolicyStoreOutput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetPolicyStoreOutput.policy_store_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetPolicyStoreOutput.arn required")
    if "validationSettings" in data:
        import aws_sdk_verifiedpermissions.types.validation_settings

        out["validation_settings"] = (
            aws_sdk_verifiedpermissions.types.validation_settings.deserialize_aws_json_1_0(
                data["validationSettings"]
            )
        )
    else:
        raise DeserializationError("GetPolicyStoreOutput.validation_settings required")
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("GetPolicyStoreOutput.created_date required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("GetPolicyStoreOutput.last_updated_date required")
    if "description" in data:
        out["description"] = data["description"]
    if "deletionProtection" in data:
        import aws_sdk_verifiedpermissions.types.deletion_protection

        out["deletion_protection"] = (
            aws_sdk_verifiedpermissions.types.deletion_protection.deserialize_aws_json_1_0(
                data["deletionProtection"]
            )
        )
    if "encryptionState" in data:
        import aws_sdk_verifiedpermissions.types.encryption_state

        out["encryption_state"] = (
            aws_sdk_verifiedpermissions.types.encryption_state.deserialize_aws_json_1_0(
                data["encryptionState"]
            )
        )
    if "cedarVersion" in data:
        import aws_sdk_verifiedpermissions.types.cedar_version

        out["cedar_version"] = (
            aws_sdk_verifiedpermissions.types.cedar_version.deserialize_aws_json_1_0(
                data["cedarVersion"]
            )
        )
    if "tags" in data:
        import aws_sdk_verifiedpermissions.types.tag_map

        out["tags"] = (
            aws_sdk_verifiedpermissions.types.tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out

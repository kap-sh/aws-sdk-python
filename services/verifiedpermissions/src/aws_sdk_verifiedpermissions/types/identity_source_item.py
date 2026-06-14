"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySourceItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.configuration_item
    import aws_sdk_verifiedpermissions.types.identity_source_id
    import aws_sdk_verifiedpermissions.types.identity_source_item_details
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.principal_entity_type
    import aws_sdk_verifiedpermissions.types.timestamp_format


class IdentitySourceItem(TypedDict):
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the identity source was originally created.</p>"""
    details: NotRequired[
        "aws_sdk_verifiedpermissions.types.identity_source_item_details.IdentitySourceItemDetails"
    ]
    """<p>A structure that contains the details of the associated identity provider (IdP).</p>"""
    identity_source_id: (
        "aws_sdk_verifiedpermissions.types.identity_source_id.IdentitySourceId"
    )
    """<p>The unique identifier of the identity source.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time the identity source was most recently updated.</p>"""
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The identifier of the policy store that contains the identity source.</p>"""
    principal_entity_type: (
        "aws_sdk_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    )
    """<p>The Cedar entity type of the principals returned from the IdP associated with this identity source.</p>"""
    configuration: NotRequired[
        "aws_sdk_verifiedpermissions.types.configuration_item.ConfigurationItem"
    ]
    """<p>Contains configuration information about an identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySourceItem) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    if "details" in value:
        import aws_sdk_verifiedpermissions.types.identity_source_item_details

        out["details"] = (
            aws_sdk_verifiedpermissions.types.identity_source_item_details.serialize_aws_json_1_0(
                value["details"]
            )
        )
    out["identitySourceId"] = value["identity_source_id"]
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    out["policyStoreId"] = value["policy_store_id"]
    out["principalEntityType"] = value["principal_entity_type"]
    if "configuration" in value:
        import aws_sdk_verifiedpermissions.types.configuration_item

        out["configuration"] = (
            aws_sdk_verifiedpermissions.types.configuration_item.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdentitySourceItem:
    out: IdentitySourceItem = {}  # type: ignore[typeddict-item]
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("IdentitySourceItem.created_date required")
    if "details" in data:
        import aws_sdk_verifiedpermissions.types.identity_source_item_details

        out["details"] = (
            aws_sdk_verifiedpermissions.types.identity_source_item_details.deserialize_aws_json_1_0(
                data["details"]
            )
        )
    if "identitySourceId" in data:
        out["identity_source_id"] = data["identitySourceId"]
    else:
        raise DeserializationError("IdentitySourceItem.identity_source_id required")
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("IdentitySourceItem.last_updated_date required")
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("IdentitySourceItem.policy_store_id required")
    if "principalEntityType" in data:
        out["principal_entity_type"] = data["principalEntityType"]
    else:
        raise DeserializationError("IdentitySourceItem.principal_entity_type required")
    if "configuration" in data:
        import aws_sdk_verifiedpermissions.types.configuration_item

        out["configuration"] = (
            aws_sdk_verifiedpermissions.types.configuration_item.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out

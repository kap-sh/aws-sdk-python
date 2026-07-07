"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetIdentitySourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.configuration_detail
    import aws_sdk_verifiedpermissions.types.identity_source_details
    import aws_sdk_verifiedpermissions.types.identity_source_id
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.principal_entity_type
    import aws_sdk_verifiedpermissions.types.timestamp_format


class GetIdentitySourceOutput(TypedDict, closed=True):
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the identity source was originally created.</p>"""
    details: NotRequired[
        "aws_sdk_verifiedpermissions.types.identity_source_details.IdentitySourceDetails"
    ]
    """<p>A structure that describes the configuration of the identity source.</p>"""
    identity_source_id: (
        "aws_sdk_verifiedpermissions.types.identity_source_id.IdentitySourceId"
    )
    """<p>The ID of the identity source.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time that the identity source was most recently updated.</p>"""
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the identity source.</p>"""
    principal_entity_type: (
        "aws_sdk_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    )
    """<p>The data type of principals generated for identities authenticated by this identity source.</p>"""
    configuration: NotRequired[
        "aws_sdk_verifiedpermissions.types.configuration_detail.ConfigurationDetail"
    ]
    """<p>Contains configuration information about an identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIdentitySourceOutput) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    if "details" in value:
        import aws_sdk_verifiedpermissions.types.identity_source_details

        out["details"] = (
            aws_sdk_verifiedpermissions.types.identity_source_details.serialize_aws_json_1_0(
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
        import aws_sdk_verifiedpermissions.types.configuration_detail

        out["configuration"] = (
            aws_sdk_verifiedpermissions.types.configuration_detail.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIdentitySourceOutput:
    out: GetIdentitySourceOutput = {}  # type: ignore[typeddict-item]
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("GetIdentitySourceOutput.created_date required")
    if "details" in data:
        import aws_sdk_verifiedpermissions.types.identity_source_details

        out["details"] = (
            aws_sdk_verifiedpermissions.types.identity_source_details.deserialize_aws_json_1_0(
                data["details"]
            )
        )
    if "identitySourceId" in data:
        out["identity_source_id"] = data["identitySourceId"]
    else:
        raise DeserializationError(
            "GetIdentitySourceOutput.identity_source_id required"
        )
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("GetIdentitySourceOutput.last_updated_date required")
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetIdentitySourceOutput.policy_store_id required")
    if "principalEntityType" in data:
        out["principal_entity_type"] = data["principalEntityType"]
    else:
        raise DeserializationError(
            "GetIdentitySourceOutput.principal_entity_type required"
        )
    if "configuration" in data:
        import aws_sdk_verifiedpermissions.types.configuration_detail

        out["configuration"] = (
            aws_sdk_verifiedpermissions.types.configuration_detail.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out

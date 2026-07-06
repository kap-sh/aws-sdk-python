"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreateIdentitySourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.identity_source_id
    import aws_sdk_verifiedpermissions.types.policy_store_id
    import aws_sdk_verifiedpermissions.types.timestamp_format


class CreateIdentitySourceOutput(TypedDict, closed=True):
    created_date: "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the identity source was originally created.</p>"""
    identity_source_id: (
        "aws_sdk_verifiedpermissions.types.identity_source_id.IdentitySourceId"
    )
    """<p>The unique ID of the new identity source.</p>"""
    last_updated_date: (
        "aws_sdk_verifiedpermissions.types.timestamp_format.TimestampFormat"
    )
    """<p>The date and time the identity source was most recently updated.</p>"""
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIdentitySourceOutput) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        aws_sdk_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIdentitySourceOutput:
    out: CreateIdentitySourceOutput = {}  # type: ignore[typeddict-item]
    if "createdDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("CreateIdentitySourceOutput.created_date required")
    if "identitySourceId" in data:
        out["identity_source_id"] = data["identitySourceId"]
    else:
        raise DeserializationError(
            "CreateIdentitySourceOutput.identity_source_id required"
        )
    if "lastUpdatedDate" in data:
        import aws_sdk_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            aws_sdk_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdentitySourceOutput.last_updated_date required"
        )
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError(
            "CreateIdentitySourceOutput.policy_store_id required"
        )
    return out

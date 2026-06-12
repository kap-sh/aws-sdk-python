"""Generated from Smithy shape ``com.amazonaws.identitystore#GetUserIdRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.alternate_identifier
    import aws_sdk_identitystore.types.identity_store_id


class GetUserIdRequest(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    alternate_identifier: (
        "aws_sdk_identitystore.types.alternate_identifier.AlternateIdentifier"
    )
    """<p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid paths are <code> userName</code> and <code>emails.value</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserIdRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    import aws_sdk_identitystore.types.alternate_identifier

    out["AlternateIdentifier"] = (
        aws_sdk_identitystore.types.alternate_identifier.serialize_aws_json_1_1(
            value["alternate_identifier"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserIdRequest:
    out: GetUserIdRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("GetUserIdRequest.identity_store_id required")
    if "AlternateIdentifier" in data:
        import aws_sdk_identitystore.types.alternate_identifier

        out["alternate_identifier"] = (
            aws_sdk_identitystore.types.alternate_identifier.deserialize_aws_json_1_1(
                data["AlternateIdentifier"]
            )
        )
    else:
        raise DeserializationError("GetUserIdRequest.alternate_identifier required")
    return out

"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.extension_names
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.resource_id


class DescribeUserRequest(TypedDict, closed=True):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>"""
    user_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p>"""
    extensions: NotRequired[
        "aws_sdk_identitystore.types.extension_names.ExtensionNames"
    ]
    """<p>A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    if "extensions" in value:
        import aws_sdk_identitystore.types.extension_names

        out["Extensions"] = (
            aws_sdk_identitystore.types.extension_names.serialize_aws_json_1_1(
                value["extensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserRequest:
    out: DescribeUserRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("DescribeUserRequest.identity_store_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("DescribeUserRequest.user_id required")
    if "Extensions" in data:
        import aws_sdk_identitystore.types.extension_names

        out["extensions"] = (
            aws_sdk_identitystore.types.extension_names.deserialize_aws_json_1_1(
                data["Extensions"]
            )
        )
    return out

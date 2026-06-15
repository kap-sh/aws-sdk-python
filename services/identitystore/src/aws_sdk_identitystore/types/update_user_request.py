"""Generated from Smithy shape ``com.amazonaws.identitystore#UpdateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.attribute_operations
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.resource_id


class UpdateUserRequest(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    user_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p>"""
    operations: "aws_sdk_identitystore.types.attribute_operations.AttributeOperations"
    r"""<p>A list of <code>AttributeOperation</code> objects to apply to the requested user. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html\">User</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    import aws_sdk_identitystore.types.attribute_operations

    out["Operations"] = (
        aws_sdk_identitystore.types.attribute_operations.serialize_aws_json_1_1(
            value["operations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("UpdateUserRequest.identity_store_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("UpdateUserRequest.user_id required")
    if "Operations" in data:
        import aws_sdk_identitystore.types.attribute_operations

        out["operations"] = (
            aws_sdk_identitystore.types.attribute_operations.deserialize_aws_json_1_1(
                data["Operations"]
            )
        )
    else:
        raise DeserializationError("UpdateUserRequest.operations required")
    return out

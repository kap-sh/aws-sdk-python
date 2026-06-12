"""Generated from Smithy shape ``com.amazonaws.identitystore#IsMemberInGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.group_ids
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.member_id


class IsMemberInGroupsRequest(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    member_id: "aws_sdk_identitystore.types.member_id.MemberId"
    """<p>An object containing the identifier of a group member.</p>"""
    group_ids: "aws_sdk_identitystore.types.group_ids.GroupIds"
    """<p>A list of identifiers for groups in the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsMemberInGroupsRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    import aws_sdk_identitystore.types.member_id

    out["MemberId"] = aws_sdk_identitystore.types.member_id.serialize_aws_json_1_1(
        value["member_id"]
    )
    import aws_sdk_identitystore.types.group_ids

    out["GroupIds"] = aws_sdk_identitystore.types.group_ids.serialize_aws_json_1_1(
        value["group_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IsMemberInGroupsRequest:
    out: IsMemberInGroupsRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("IsMemberInGroupsRequest.identity_store_id required")
    if "MemberId" in data:
        import aws_sdk_identitystore.types.member_id

        out["member_id"] = (
            aws_sdk_identitystore.types.member_id.deserialize_aws_json_1_1(
                data["MemberId"]
            )
        )
    else:
        raise DeserializationError("IsMemberInGroupsRequest.member_id required")
    if "GroupIds" in data:
        import aws_sdk_identitystore.types.group_ids

        out["group_ids"] = (
            aws_sdk_identitystore.types.group_ids.deserialize_aws_json_1_1(
                data["GroupIds"]
            )
        )
    else:
        raise DeserializationError("IsMemberInGroupsRequest.group_ids required")
    return out

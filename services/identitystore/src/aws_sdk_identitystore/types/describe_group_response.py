"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.date_type
    import aws_sdk_identitystore.types.external_ids
    import aws_sdk_identitystore.types.group_display_name
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.resource_id
    import aws_sdk_identitystore.types.sensitive_string_type
    import aws_sdk_identitystore.types.string_type


class DescribeGroupResponse(TypedDict):
    group_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p>"""
    display_name: NotRequired[
        "aws_sdk_identitystore.types.group_display_name.GroupDisplayName"
    ]
    """<p>The group’s display name value. The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, and nonbreaking space in this attribute. This value is specified at the time that the group is created and stored as an attribute of the group object in the identity store.</p>"""
    external_ids: NotRequired["aws_sdk_identitystore.types.external_ids.ExternalIds"]
    """<p>A list of <code>ExternalId</code> objects that contains the identifiers issued to this resource by an external identity provider.</p>"""
    description: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing a description of the group.</p>"""
    created_at: NotRequired["aws_sdk_identitystore.types.date_type.DateType"]
    """<p>The date and time the group was created.</p>"""
    updated_at: NotRequired["aws_sdk_identitystore.types.date_type.DateType"]
    """<p>The date and time the group was last updated.</p>"""
    created_by: NotRequired["aws_sdk_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that created the group.</p>"""
    updated_by: NotRequired["aws_sdk_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that last updated the group.</p>"""
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGroupResponse) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "external_ids" in value:
        import aws_sdk_identitystore.types.external_ids

        out["ExternalIds"] = (
            aws_sdk_identitystore.types.external_ids.serialize_aws_json_1_1(
                value["external_ids"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_identitystore.types.date_type

        out["CreatedAt"] = aws_sdk_identitystore.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_identitystore.types.date_type

        out["UpdatedAt"] = aws_sdk_identitystore.types.date_type.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    out["IdentityStoreId"] = value["identity_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGroupResponse:
    out: DescribeGroupResponse = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DescribeGroupResponse.group_id required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "ExternalIds" in data:
        import aws_sdk_identitystore.types.external_ids

        out["external_ids"] = (
            aws_sdk_identitystore.types.external_ids.deserialize_aws_json_1_1(
                data["ExternalIds"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_identitystore.types.date_type

        out["created_at"] = (
            aws_sdk_identitystore.types.date_type.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_identitystore.types.date_type

        out["updated_at"] = (
            aws_sdk_identitystore.types.date_type.deserialize_aws_json_1_1(
                data["UpdatedAt"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "UpdatedBy" in data:
        out["updated_by"] = data["UpdatedBy"]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("DescribeGroupResponse.identity_store_id required")
    return out

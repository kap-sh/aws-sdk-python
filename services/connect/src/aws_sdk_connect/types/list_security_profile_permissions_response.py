"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityProfilePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.permissions_list
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class ListSecurityProfilePermissionsResponse(TypedDict, closed=True):
    permissions: NotRequired["aws_sdk_connect.types.permissions_list.PermissionsList"]
    r"""<p>The permissions granted to the security profile. For a complete list of valid permissions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html\">List of security profile permissions</a>.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilePermissionsResponse) -> dict:
    out: dict = {}
    if "permissions" in value:
        import aws_sdk_connect.types.permissions_list

        out["Permissions"] = aws_sdk_connect.types.permissions_list.serialize_json(
            value["permissions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfilePermissionsResponse:
    out: ListSecurityProfilePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Permissions" in data:
        import aws_sdk_connect.types.permissions_list

        out["permissions"] = aws_sdk_connect.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out

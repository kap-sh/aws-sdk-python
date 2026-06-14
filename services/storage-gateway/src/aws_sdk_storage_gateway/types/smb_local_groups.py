"""Generated from Smithy shape ``com.amazonaws.storagegateway#SMBLocalGroups``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.user_list


class SMBLocalGroups(TypedDict):
    gateway_admins: NotRequired["aws_sdk_storage_gateway.types.user_list.UserList"]
    r"""<p>A list of Active Directory users and groups that have local Gateway Admin permissions. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>DOMAIN\group1</code>, and <code>group1</code>.</p> <p>Gateway Admins can use the Shared Folders Microsoft Management Console snap-in to force-close files that are open and locked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SMBLocalGroups) -> dict:
    out: dict = {}
    if "gateway_admins" in value:
        import aws_sdk_storage_gateway.types.user_list

        out["GatewayAdmins"] = (
            aws_sdk_storage_gateway.types.user_list.serialize_aws_json_1_1(
                value["gateway_admins"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SMBLocalGroups:
    out: SMBLocalGroups = {}  # type: ignore[typeddict-item]
    if "GatewayAdmins" in data:
        import aws_sdk_storage_gateway.types.user_list

        out["gateway_admins"] = (
            aws_sdk_storage_gateway.types.user_list.deserialize_aws_json_1_1(
                data["GatewayAdmins"]
            )
        )
    return out

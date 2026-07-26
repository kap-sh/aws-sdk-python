"""Generated from Smithy shape ``com.amazonaws.storagegateway#SMBLocalGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.user_list


class SMBLocalGroups(TypedDict, closed=True):
    gateway_admins: NotRequired["capo_storage_gateway.types.user_list.UserList"]
    r"""<p>A list of Active Directory users and groups that have local Gateway Admin permissions. Acceptable formats include: <code>DOMAIN\User1</code>, <code>user1</code>, <code>DOMAIN\group1</code>, and <code>group1</code>.</p> <p>Gateway Admins can use the Shared Folders Microsoft Management Console snap-in to force-close files that are open and locked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SMBLocalGroups) -> dict:
    out: dict = {}
    if "gateway_admins" in value:
        import capo_storage_gateway.types.user_list

        out["GatewayAdmins"] = (
            capo_storage_gateway.types.user_list.serialize_aws_json_1_1(
                value["gateway_admins"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SMBLocalGroups:
    out: SMBLocalGroups = {}  # type: ignore[typeddict-item]
    if "GatewayAdmins" in data:
        import capo_storage_gateway.types.user_list

        out["gateway_admins"] = (
            capo_storage_gateway.types.user_list.deserialize_aws_json_1_1(
                data["GatewayAdmins"]
            )
        )
    return out

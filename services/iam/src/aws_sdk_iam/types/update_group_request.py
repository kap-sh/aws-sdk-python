"""Generated from Smithy shape ``com.amazonaws.iam#UpdateGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.group_name_type
    import aws_sdk_iam.types.path_type


class UpdateGroupRequest(TypedDict):
    group_name: "aws_sdk_iam.types.group_name_type.groupNameType"
    r"""<p>Name of the IAM group to update. If you're changing the name of the group, this is the original name.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    new_path: NotRequired["aws_sdk_iam.types.path_type.pathType"]
    r"""<p>New path for the IAM group. Only include this if changing the group's path.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    new_group_name: NotRequired["aws_sdk_iam.types.group_name_type.groupNameType"]
    r"""<p>New name for the IAM group. Only include this if changing the group's name.</p> <p>IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both \"MyResource\" and \"myresource\".</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateGroupRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    if "new_path" in value:
        pairs.append((f"{prefix}.NewPath", str(value["new_path"])))
    if "new_group_name" in value:
        pairs.append((f"{prefix}.NewGroupName", str(value["new_group_name"])))


def deserialize_query(el: Element) -> UpdateGroupRequest:
    out: UpdateGroupRequest = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    else:
        raise DeserializationError("UpdateGroupRequest.group_name required")
    child_new_path = el.find("NewPath")
    if child_new_path is not None:
        out["new_path"] = str(child_new_path.text or "")
    child_new_group_name = el.find("NewGroupName")
    if child_new_group_name is not None:
        out["new_group_name"] = str(child_new_group_name.text or "")
    return out

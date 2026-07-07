"""Generated from Smithy shape ``com.amazonaws.iam#TagRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.role_name_type
    import aws_sdk_iam.types.tag_list_type


class TagRoleRequest(TypedDict, closed=True):
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    r"""<p>The name of the IAM role to which you want to add tags.</p> <p>This parameter accepts (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "aws_sdk_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM role. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))
    import aws_sdk_iam.types.tag_list_type

    aws_sdk_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{prefix}.Tags"
    )


def deserialize_query(el: Element) -> TagRoleRequest:
    out: TagRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("TagRoleRequest.role_name required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagRoleRequest.tags required")
    return out

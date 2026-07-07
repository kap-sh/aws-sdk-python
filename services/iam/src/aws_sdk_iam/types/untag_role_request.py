"""Generated from Smithy shape ``com.amazonaws.iam#UntagRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.role_name_type
    import aws_sdk_iam.types.tag_key_list_type


class UntagRoleRequest(TypedDict, closed=True):
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    r"""<p>The name of the IAM role from which you want to remove tags.</p> <p>This parameter accepts (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tag_keys: "aws_sdk_iam.types.tag_key_list_type.tagKeyListType"
    """<p>A list of key names as a simple array of strings. The tags with matching keys are removed from the specified role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))
    import aws_sdk_iam.types.tag_key_list_type

    aws_sdk_iam.types.tag_key_list_type.serialize_query(
        value["tag_keys"], pairs, f"{prefix}.TagKeys"
    )


def deserialize_query(el: Element) -> UntagRoleRequest:
    out: UntagRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("UntagRoleRequest.role_name required")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_iam.types.tag_key_list_type

        out["tag_keys"] = aws_sdk_iam.types.tag_key_list_type.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagRoleRequest.tag_keys required")
    return out

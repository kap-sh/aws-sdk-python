"""Generated from Smithy shape ``com.amazonaws.iam#ChangePasswordRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.password_type


class ChangePasswordRequest(TypedDict):
    old_password: "aws_sdk_iam.types.password_type.passwordType"
    """<p>The IAM user's current password.</p>"""
    new_password: "aws_sdk_iam.types.password_type.passwordType"
    r"""<p>The new password. The new password must conform to the Amazon Web Services account's password policy, if one exists.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> that is used to validate this parameter is a string of characters. That string can include almost any printable ASCII character from the space (<code>\u0020</code>) through the end of the ASCII character range (<code>\u00FF</code>). You can also include the tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>) characters. Any of these characters are valid in a password. However, many tools, such as the Amazon Web Services Management Console, might restrict the ability to type certain characters because they have special meaning within that tool.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangePasswordRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.OldPassword", str(value["old_password"])))
    pairs.append((f"{prefix}.NewPassword", str(value["new_password"])))


def deserialize_query(el: Element) -> ChangePasswordRequest:
    out: ChangePasswordRequest = {}  # type: ignore[typeddict-item]
    child_old_password = el.find("OldPassword")
    if child_old_password is not None:
        out["old_password"] = str(child_old_password.text or "")
    else:
        raise DeserializationError("ChangePasswordRequest.old_password required")
    child_new_password = el.find("NewPassword")
    if child_new_password is not None:
        out["new_password"] = str(child_new_password.text or "")
    else:
        raise DeserializationError("ChangePasswordRequest.new_password required")
    return out

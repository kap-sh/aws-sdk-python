"""Generated from Smithy shape ``com.amazonaws.iam#DeleteUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.existing_user_name_type


class DeleteUserRequest(TypedDict):
    user_name: "aws_sdk_iam.types.existing_user_name_type.existingUserNameType"
    r"""<p>The name of the user to delete.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteUserRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))


def deserialize_query(el: Element) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("DeleteUserRequest.user_name required")
    return out

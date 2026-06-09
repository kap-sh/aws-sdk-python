"""Generated from Smithy shape ``com.amazonaws.iam#UntagUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.existing_user_name_type
    import aws_sdk_iam.types.tag_key_list_type


class UntagUserRequest(TypedDict):
    user_name: "aws_sdk_iam.types.existing_user_name_type.existingUserNameType"
    """<p>The name of the IAM user from which you want to remove tags.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tag_keys: "aws_sdk_iam.types.tag_key_list_type.tagKeyListType"
    """<p>A list of key names as a simple array of strings. The tags with matching keys are removed from the specified user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagUserRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    import aws_sdk_iam.types.tag_key_list_type

    aws_sdk_iam.types.tag_key_list_type.serialize_query(
        value["tag_keys"], pairs, f"{prefix}.TagKeys"
    )


def deserialize_query(el: Element) -> UntagUserRequest:
    out: UntagUserRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("UntagUserRequest.user_name required")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_iam.types.tag_key_list_type

        out["tag_keys"] = aws_sdk_iam.types.tag_key_list_type.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagUserRequest.tag_keys required")
    return out

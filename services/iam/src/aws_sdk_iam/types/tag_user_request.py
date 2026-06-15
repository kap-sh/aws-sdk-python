"""Generated from Smithy shape ``com.amazonaws.iam#TagUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.existing_user_name_type
    import aws_sdk_iam.types.tag_list_type


class TagUserRequest(TypedDict):
    user_name: "aws_sdk_iam.types.existing_user_name_type.existingUserNameType"
    r"""<p>The name of the IAM user to which you want to add tags.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "aws_sdk_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM user. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagUserRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    import aws_sdk_iam.types.tag_list_type

    aws_sdk_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{prefix}.Tags"
    )


def deserialize_query(el: Element) -> TagUserRequest:
    out: TagUserRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("TagUserRequest.user_name required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagUserRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.iam#TagInstanceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.instance_profile_name_type
    import aws_sdk_iam.types.tag_list_type


class TagInstanceProfileRequest(TypedDict):
    instance_profile_name: (
        "aws_sdk_iam.types.instance_profile_name_type.instanceProfileNameType"
    )
    """<p>The name of the IAM instance profile to which you want to add tags.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "aws_sdk_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM instance profile. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagInstanceProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.InstanceProfileName", str(value["instance_profile_name"])))
    import aws_sdk_iam.types.tag_list_type

    aws_sdk_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{prefix}.Tags"
    )


def deserialize_query(el: Element) -> TagInstanceProfileRequest:
    out: TagInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    child_instance_profile_name = el.find("InstanceProfileName")
    if child_instance_profile_name is not None:
        out["instance_profile_name"] = str(child_instance_profile_name.text or "")
    else:
        raise DeserializationError(
            "TagInstanceProfileRequest.instance_profile_name required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagInstanceProfileRequest.tags required")
    return out

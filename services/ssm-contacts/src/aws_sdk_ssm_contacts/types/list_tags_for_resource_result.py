"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.tags_list


class ListTagsForResourceResult(TypedDict):
    tags: NotRequired["aws_sdk_ssm_contacts.types.tags_list.TagsList"]
    """<p>The tags related to the contact or escalation plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_ssm_contacts.types.tags_list

        out["Tags"] = aws_sdk_ssm_contacts.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_ssm_contacts.types.tags_list

        out["tags"] = aws_sdk_ssm_contacts.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.tags_list


class ListTagsForResourceResult(TypedDict, closed=True):
    tags: NotRequired["capo_ssm_contacts.types.tags_list.TagsList"]
    """<p>The tags related to the contact or escalation plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_ssm_contacts.types.tags_list

        out["Tags"] = capo_ssm_contacts.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_ssm_contacts.types.tags_list

        out["tags"] = capo_ssm_contacts.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

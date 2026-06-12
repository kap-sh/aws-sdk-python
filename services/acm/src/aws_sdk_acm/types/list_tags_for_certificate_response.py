"""Generated from Smithy shape ``com.amazonaws.acm#ListTagsForCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.tag_list


class ListTagsForCertificateResponse(TypedDict):
    tags: NotRequired["aws_sdk_acm.types.tag_list.TagList"]
    """<p>The key-value pairs that define the applied tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForCertificateResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_acm.types.tag_list

        out["Tags"] = aws_sdk_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForCertificateResponse:
    out: ListTagsForCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_acm.types.tag_list

        out["tags"] = aws_sdk_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out

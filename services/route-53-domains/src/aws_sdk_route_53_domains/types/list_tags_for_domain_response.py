"""Generated from Smithy shape ``com.amazonaws.route53domains#ListTagsForDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.tag_list


class ListTagsForDomainResponse(TypedDict, closed=True):
    tag_list: NotRequired["aws_sdk_route_53_domains.types.tag_list.TagList"]
    """<p>A list of the tags that are associated with the specified domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForDomainResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import aws_sdk_route_53_domains.types.tag_list

        out["TagList"] = aws_sdk_route_53_domains.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForDomainResponse:
    out: ListTagsForDomainResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_route_53_domains.types.tag_list

        out["tag_list"] = (
            aws_sdk_route_53_domains.types.tag_list.deserialize_aws_json_1_1(
                data["TagList"]
            )
        )
    return out

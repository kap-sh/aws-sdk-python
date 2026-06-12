"""Generated from Smithy shape ``com.amazonaws.servicequotas#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.output_tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_service_quotas.types.output_tags.OutputTags"]
    """<p>A complex data type that contains zero or more tag elements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_service_quotas.types.output_tags

        out["Tags"] = aws_sdk_service_quotas.types.output_tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_service_quotas.types.output_tags

        out["tags"] = aws_sdk_service_quotas.types.output_tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

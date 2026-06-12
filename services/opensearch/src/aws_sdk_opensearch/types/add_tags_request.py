"""Generated from Smithy shape ``com.amazonaws.opensearch#AddTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn
    import aws_sdk_opensearch.types.tag_list


class AddTagsRequest(TypedDict):
    arn: "aws_sdk_opensearch.types.arn.ARN"
    """<p>Amazon Resource Name (ARN) for the OpenSearch Service domain, data source, or application to which you want to attach resource tags.</p>"""
    tag_list: "aws_sdk_opensearch.types.tag_list.TagList"
    """<p>List of resource tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddTagsRequest) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    import aws_sdk_opensearch.types.tag_list

    out["TagList"] = aws_sdk_opensearch.types.tag_list.serialize_json(value["tag_list"])
    return out


def deserialize_json(data: dict) -> AddTagsRequest:
    out: AddTagsRequest = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("AddTagsRequest.arn required")
    if "TagList" in data:
        import aws_sdk_opensearch.types.tag_list

        out["tag_list"] = aws_sdk_opensearch.types.tag_list.deserialize_json(
            data["TagList"]
        )
    else:
        raise DeserializationError("AddTagsRequest.tag_list required")
    return out

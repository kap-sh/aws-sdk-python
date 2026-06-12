"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RemoveTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.arn
    import aws_sdk_elasticsearch_service.types.string_list


class RemoveTagsRequest(TypedDict):
    arn: "aws_sdk_elasticsearch_service.types.arn.ARN"
    """<p>Specifies the <code>ARN</code> for the Elasticsearch domain from which you want to delete the specified tags.</p>"""
    tag_keys: "aws_sdk_elasticsearch_service.types.string_list.StringList"
    """<p>Specifies the <code>TagKey</code> list which you want to remove from the Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveTagsRequest) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    import aws_sdk_elasticsearch_service.types.string_list

    out["TagKeys"] = aws_sdk_elasticsearch_service.types.string_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> RemoveTagsRequest:
    out: RemoveTagsRequest = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("RemoveTagsRequest.arn required")
    if "TagKeys" in data:
        import aws_sdk_elasticsearch_service.types.string_list

        out["tag_keys"] = (
            aws_sdk_elasticsearch_service.types.string_list.deserialize_json(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("RemoveTagsRequest.tag_keys required")
    return out

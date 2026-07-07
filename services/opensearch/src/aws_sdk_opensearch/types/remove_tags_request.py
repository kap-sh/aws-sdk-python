"""Generated from Smithy shape ``com.amazonaws.opensearch#RemoveTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn
    import aws_sdk_opensearch.types.string_list


class RemoveTagsRequest(TypedDict, closed=True):
    arn: "aws_sdk_opensearch.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the domain, data source, or application from which you want to delete the specified tags.</p>"""
    tag_keys: "aws_sdk_opensearch.types.string_list.StringList"
    """<p>The list of tag keys to remove from the domain, data source, or application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveTagsRequest) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    import aws_sdk_opensearch.types.string_list

    out["TagKeys"] = aws_sdk_opensearch.types.string_list.serialize_json(
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
        import aws_sdk_opensearch.types.string_list

        out["tag_keys"] = aws_sdk_opensearch.types.string_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("RemoveTagsRequest.tag_keys required")
    return out

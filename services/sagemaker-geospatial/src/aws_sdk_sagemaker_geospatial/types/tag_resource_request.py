"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.arn
    import aws_sdk_sagemaker_geospatial.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_sagemaker_geospatial.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource you want to tag.</p>"""
    tags: "aws_sdk_sagemaker_geospatial.types.tags.Tags"
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.tags

    out["Tags"] = aws_sdk_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["tags"] = aws_sdk_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

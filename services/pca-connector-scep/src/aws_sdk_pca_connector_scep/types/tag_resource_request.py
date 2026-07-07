"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pca_connector_scep.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_pca_connector_scep.types.tags.Tags"
    """<p>The key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_pca_connector_scep.types.tags

    out["Tags"] = aws_sdk_pca_connector_scep.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_pca_connector_scep.types.tags

        out["tags"] = aws_sdk_pca_connector_scep.types.tags.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

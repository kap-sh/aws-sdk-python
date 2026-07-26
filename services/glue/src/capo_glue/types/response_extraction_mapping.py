"""Generated from Smithy shape ``com.amazonaws.glue#ResponseExtractionMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connector_property_key
    import capo_glue.types.json_path_string


class ResponseExtractionMapping(TypedDict, closed=True):
    content_path: NotRequired["capo_glue.types.json_path_string.JsonPathString"]
    """<p>A JSON path expression that specifies how to extract a value from the response body content.</p>"""
    header_key: NotRequired[
        "capo_glue.types.connector_property_key.ConnectorPropertyKey"
    ]
    """<p>The name of an HTTP response header from which to extract the value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseExtractionMapping) -> dict:
    out: dict = {}
    if "content_path" in value:
        out["ContentPath"] = value["content_path"]
    if "header_key" in value:
        out["HeaderKey"] = value["header_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseExtractionMapping:
    out: ResponseExtractionMapping = {}  # type: ignore[typeddict-item]
    if "ContentPath" in data:
        out["content_path"] = data["ContentPath"]
    if "HeaderKey" in data:
        out["header_key"] = data["HeaderKey"]
    return out

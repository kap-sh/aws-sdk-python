"""Generated from Smithy shape ``com.amazonaws.bedrock#RequestMetadataBaseFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.request_metadata_map


class RequestMetadataBaseFilters(TypedDict, closed=True):
    equals: NotRequired["aws_sdk_bedrock.types.request_metadata_map.RequestMetadataMap"]
    """<p>Include results where the key equals the value.</p>"""
    not_equals: NotRequired[
        "aws_sdk_bedrock.types.request_metadata_map.RequestMetadataMap"
    ]
    """<p>Include results where the key does not equal the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestMetadataBaseFilters) -> dict:
    out: dict = {}
    if "equals" in value:
        import aws_sdk_bedrock.types.request_metadata_map

        out["equals"] = aws_sdk_bedrock.types.request_metadata_map.serialize_json(
            value["equals"]
        )
    if "not_equals" in value:
        import aws_sdk_bedrock.types.request_metadata_map

        out["notEquals"] = aws_sdk_bedrock.types.request_metadata_map.serialize_json(
            value["not_equals"]
        )
    return out


def deserialize_json(data: dict) -> RequestMetadataBaseFilters:
    out: RequestMetadataBaseFilters = {}  # type: ignore[typeddict-item]
    if "equals" in data:
        import aws_sdk_bedrock.types.request_metadata_map

        out["equals"] = aws_sdk_bedrock.types.request_metadata_map.deserialize_json(
            data["equals"]
        )
    if "notEquals" in data:
        import aws_sdk_bedrock.types.request_metadata_map

        out["not_equals"] = aws_sdk_bedrock.types.request_metadata_map.deserialize_json(
            data["notEquals"]
        )
    return out

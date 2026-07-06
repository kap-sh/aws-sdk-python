"""Generated from Smithy shape ``com.amazonaws.medialive#CreateSdiSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.sdi_source_mode
    import aws_sdk_medialive.types.sdi_source_type
    import aws_sdk_medialive.types.tags


class CreateSdiSourceRequest(TypedDict, closed=True):
    mode: NotRequired["aws_sdk_medialive.types.sdi_source_mode.SdiSourceMode"]
    """Applies only if the type is QUAD. Specify the mode for handling the quad-link signal: QUADRANT or INTERLEAVE."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive."""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An ID that you assign to a create request. This ID ensures idempotency when creating resources."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    type: NotRequired["aws_sdk_medialive.types.sdi_source_type.SdiSourceType"]
    """Specify the type of the SDI source: SINGLE: The source is a single-link source. QUAD: The source is one part of a quad-link source."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSdiSourceRequest) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_medialive.types.sdi_source_mode

        out["mode"] = aws_sdk_medialive.types.sdi_source_mode.serialize_json(
            value["mode"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    if "type" in value:
        import aws_sdk_medialive.types.sdi_source_type

        out["type"] = aws_sdk_medialive.types.sdi_source_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> CreateSdiSourceRequest:
    out: CreateSdiSourceRequest = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_medialive.types.sdi_source_mode

        out["mode"] = aws_sdk_medialive.types.sdi_source_mode.deserialize_json(
            data["mode"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    if "type" in data:
        import aws_sdk_medialive.types.sdi_source_type

        out["type"] = aws_sdk_medialive.types.sdi_source_type.deserialize_json(
            data["type"]
        )
    return out

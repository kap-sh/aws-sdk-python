"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateSdiSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.sdi_source_mode
    import aws_sdk_medialive.types.sdi_source_type


class UpdateSdiSourceRequest(TypedDict):
    mode: NotRequired["aws_sdk_medialive.types.sdi_source_mode.SdiSourceMode"]
    """Include this parameter only if you want to change the name of the SdiSource. Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Include this parameter only if you want to change the name of the SdiSource. Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive."""
    sdi_source_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the SdiSource"""
    type: NotRequired["aws_sdk_medialive.types.sdi_source_type.SdiSourceType"]
    """Include this parameter only if you want to change the mode. Specify the type of the SDI source: SINGLE: The source is a single-link source. QUAD: The source is one part of a quad-link source."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSdiSourceRequest) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_medialive.types.sdi_source_mode

        out["mode"] = aws_sdk_medialive.types.sdi_source_mode.serialize_json(
            value["mode"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_medialive.types.sdi_source_type

        out["type"] = aws_sdk_medialive.types.sdi_source_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSdiSourceRequest:
    out: UpdateSdiSourceRequest = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_medialive.types.sdi_source_mode

        out["mode"] = aws_sdk_medialive.types.sdi_source_mode.deserialize_json(
            data["mode"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_medialive.types.sdi_source_type

        out["type"] = aws_sdk_medialive.types.sdi_source_type.deserialize_json(
            data["type"]
        )
    return out

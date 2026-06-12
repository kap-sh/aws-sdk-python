"""Generated from Smithy shape ``com.amazonaws.medialive#CreateSdiSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.sdi_source


class CreateSdiSourceResponse(TypedDict):
    sdi_source: NotRequired["aws_sdk_medialive.types.sdi_source.SdiSource"]
    """Settings for the SDI source."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSdiSourceResponse) -> dict:
    out: dict = {}
    if "sdi_source" in value:
        import aws_sdk_medialive.types.sdi_source

        out["sdiSource"] = aws_sdk_medialive.types.sdi_source.serialize_json(
            value["sdi_source"]
        )
    return out


def deserialize_json(data: dict) -> CreateSdiSourceResponse:
    out: CreateSdiSourceResponse = {}  # type: ignore[typeddict-item]
    if "sdiSource" in data:
        import aws_sdk_medialive.types.sdi_source

        out["sdi_source"] = aws_sdk_medialive.types.sdi_source.deserialize_json(
            data["sdiSource"]
        )
    return out

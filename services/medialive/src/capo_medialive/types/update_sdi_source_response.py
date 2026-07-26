"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateSdiSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.sdi_source


class UpdateSdiSourceResponse(TypedDict, closed=True):
    sdi_source: NotRequired["capo_medialive.types.sdi_source.SdiSource"]
    """Settings for the SDI source."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSdiSourceResponse) -> dict:
    out: dict = {}
    if "sdi_source" in value:
        import capo_medialive.types.sdi_source

        out["sdiSource"] = capo_medialive.types.sdi_source.serialize_json(
            value["sdi_source"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSdiSourceResponse:
    out: UpdateSdiSourceResponse = {}  # type: ignore[typeddict-item]
    if "sdiSource" in data:
        import capo_medialive.types.sdi_source

        out["sdi_source"] = capo_medialive.types.sdi_source.deserialize_json(
            data["sdiSource"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#CdiInputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.cdi_input_resolution


class CdiInputSpecification(TypedDict, closed=True):
    resolution: NotRequired[
        "capo_medialive.types.cdi_input_resolution.CdiInputResolution"
    ]
    """Maximum CDI input resolution"""


# --- restJson1 ser/de ---
def serialize_json(value: CdiInputSpecification) -> dict:
    out: dict = {}
    if "resolution" in value:
        import capo_medialive.types.cdi_input_resolution

        out["resolution"] = capo_medialive.types.cdi_input_resolution.serialize_json(
            value["resolution"]
        )
    return out


def deserialize_json(data: dict) -> CdiInputSpecification:
    out: CdiInputSpecification = {}  # type: ignore[typeddict-item]
    if "resolution" in data:
        import capo_medialive.types.cdi_input_resolution

        out["resolution"] = capo_medialive.types.cdi_input_resolution.deserialize_json(
            data["resolution"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#CdiInputSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.cdi_input_resolution


class CdiInputSpecification(TypedDict):
    resolution: NotRequired[
        "aws_sdk_medialive.types.cdi_input_resolution.CdiInputResolution"
    ]
    """Maximum CDI input resolution"""


# --- restJson1 ser/de ---
def serialize_json(value: CdiInputSpecification) -> dict:
    out: dict = {}
    if "resolution" in value:
        import aws_sdk_medialive.types.cdi_input_resolution

        out["resolution"] = aws_sdk_medialive.types.cdi_input_resolution.serialize_json(
            value["resolution"]
        )
    return out


def deserialize_json(data: dict) -> CdiInputSpecification:
    out: CdiInputSpecification = {}  # type: ignore[typeddict-item]
    if "resolution" in data:
        import aws_sdk_medialive.types.cdi_input_resolution

        out["resolution"] = (
            aws_sdk_medialive.types.cdi_input_resolution.deserialize_json(
                data["resolution"]
            )
        )
    return out

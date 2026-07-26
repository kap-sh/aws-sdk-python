"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportErrorDetailsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.export_error_type


class ExportErrorDetailsOutput(TypedDict, closed=True):
    type: NotRequired[
        "capo_sagemaker_geospatial.types.export_error_type.ExportErrorType"
    ]
    """<p>The type of error in an export EarthObservationJob operation.</p>"""
    message: NotRequired["str"]
    """<p>A detailed message describing the error in an export EarthObservationJob operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportErrorDetailsOutput) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ExportErrorDetailsOutput:
    out: ExportErrorDetailsOutput = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out

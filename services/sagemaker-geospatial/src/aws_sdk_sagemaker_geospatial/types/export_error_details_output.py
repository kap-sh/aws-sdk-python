"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportErrorDetailsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.export_error_type


class ExportErrorDetailsOutput(TypedDict):
    type: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.export_error_type.ExportErrorType"
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

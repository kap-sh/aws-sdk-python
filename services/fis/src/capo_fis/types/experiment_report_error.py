"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_report_error_code


class ExperimentReportError(TypedDict, closed=True):
    code: NotRequired[
        "capo_fis.types.experiment_report_error_code.ExperimentReportErrorCode"
    ]
    """<p>The error code for the failed experiment report generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportError) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ExperimentReportError:
    out: ExperimentReportError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    return out

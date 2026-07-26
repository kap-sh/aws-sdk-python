"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationResultSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.file_name
    import capo_iot.types.sbom_validation_error_code
    import capo_iot.types.sbom_validation_error_message
    import capo_iot.types.sbom_validation_result


class SbomValidationResultSummary(TypedDict, closed=True):
    file_name: NotRequired["capo_iot.types.file_name.FileName"]
    """<p>The name of the SBOM file.</p>"""
    validation_result: NotRequired[
        "capo_iot.types.sbom_validation_result.SbomValidationResult"
    ]
    """<p>The end result of the SBOM validation.</p>"""
    error_code: NotRequired[
        "capo_iot.types.sbom_validation_error_code.SbomValidationErrorCode"
    ]
    """<p>The <code>errorCode</code> representing the validation failure error if the SBOM validation failed.</p>"""
    error_message: NotRequired[
        "capo_iot.types.sbom_validation_error_message.SbomValidationErrorMessage"
    ]
    """<p>The <code>errorMessage</code> representing the validation failure error if the SBOM validation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SbomValidationResultSummary) -> dict:
    out: dict = {}
    if "file_name" in value:
        out["fileName"] = value["file_name"]
    if "validation_result" in value:
        import capo_iot.types.sbom_validation_result

        out["validationResult"] = capo_iot.types.sbom_validation_result.serialize_json(
            value["validation_result"]
        )
    if "error_code" in value:
        import capo_iot.types.sbom_validation_error_code

        out["errorCode"] = capo_iot.types.sbom_validation_error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> SbomValidationResultSummary:
    out: SbomValidationResultSummary = {}  # type: ignore[typeddict-item]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    if "validationResult" in data:
        import capo_iot.types.sbom_validation_result

        out["validation_result"] = (
            capo_iot.types.sbom_validation_result.deserialize_json(
                data["validationResult"]
            )
        )
    if "errorCode" in data:
        import capo_iot.types.sbom_validation_error_code

        out["error_code"] = capo_iot.types.sbom_validation_error_code.deserialize_json(
            data["errorCode"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out

"""Generated from Smithy shape ``com.amazonaws.auditmanager#ValidateAssessmentReportIntegrityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.boolean
    import capo_auditmanager.types.string
    import capo_auditmanager.types.validation_errors


class ValidateAssessmentReportIntegrityResponse(TypedDict, closed=True):
    signature_valid: NotRequired["capo_auditmanager.types.boolean.Boolean"]
    """<p> Specifies whether the signature key is valid. </p>"""
    signature_algorithm: NotRequired["capo_auditmanager.types.string.String"]
    """<p> The signature algorithm that's used to code sign the assessment report file. </p>"""
    signature_date_time: NotRequired["capo_auditmanager.types.string.String"]
    """<p> The date and time signature that specifies when the assessment report was created. </p>"""
    signature_key_id: NotRequired["capo_auditmanager.types.string.String"]
    """<p> The unique identifier for the validation signature key. </p>"""
    validation_errors: NotRequired[
        "capo_auditmanager.types.validation_errors.ValidationErrors"
    ]
    """<p> Represents any errors that occurred when validating the assessment report. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateAssessmentReportIntegrityResponse) -> dict:
    out: dict = {}
    if "signature_valid" in value:
        out["signatureValid"] = value["signature_valid"]
    if "signature_algorithm" in value:
        out["signatureAlgorithm"] = value["signature_algorithm"]
    if "signature_date_time" in value:
        out["signatureDateTime"] = value["signature_date_time"]
    if "signature_key_id" in value:
        out["signatureKeyId"] = value["signature_key_id"]
    if "validation_errors" in value:
        import capo_auditmanager.types.validation_errors

        out["validationErrors"] = (
            capo_auditmanager.types.validation_errors.serialize_json(
                value["validation_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidateAssessmentReportIntegrityResponse:
    out: ValidateAssessmentReportIntegrityResponse = {}  # type: ignore[typeddict-item]
    if "signatureValid" in data:
        out["signature_valid"] = data["signatureValid"]
    if "signatureAlgorithm" in data:
        out["signature_algorithm"] = data["signatureAlgorithm"]
    if "signatureDateTime" in data:
        out["signature_date_time"] = data["signatureDateTime"]
    if "signatureKeyId" in data:
        out["signature_key_id"] = data["signatureKeyId"]
    if "validationErrors" in data:
        import capo_auditmanager.types.validation_errors

        out["validation_errors"] = (
            capo_auditmanager.types.validation_errors.deserialize_json(
                data["validationErrors"]
            )
        )
    return out

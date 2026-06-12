"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationResultSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.file_name
    import aws_sdk_iot.types.sbom_validation_error_code
    import aws_sdk_iot.types.sbom_validation_error_message
    import aws_sdk_iot.types.sbom_validation_result


class SbomValidationResultSummary(TypedDict):
    file_name: NotRequired["aws_sdk_iot.types.file_name.FileName"]
    """<p>The name of the SBOM file.</p>"""
    validation_result: NotRequired[
        "aws_sdk_iot.types.sbom_validation_result.SbomValidationResult"
    ]
    """<p>The end result of the SBOM validation.</p>"""
    error_code: NotRequired[
        "aws_sdk_iot.types.sbom_validation_error_code.SbomValidationErrorCode"
    ]
    """<p>The <code>errorCode</code> representing the validation failure error if the SBOM validation failed.</p>"""
    error_message: NotRequired[
        "aws_sdk_iot.types.sbom_validation_error_message.SbomValidationErrorMessage"
    ]
    """<p>The <code>errorMessage</code> representing the validation failure error if the SBOM validation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SbomValidationResultSummary) -> dict:
    out: dict = {}
    if "file_name" in value:
        out["fileName"] = value["file_name"]
    if "validation_result" in value:
        import aws_sdk_iot.types.sbom_validation_result

        out["validationResult"] = (
            aws_sdk_iot.types.sbom_validation_result.serialize_json(
                value["validation_result"]
            )
        )
    if "error_code" in value:
        import aws_sdk_iot.types.sbom_validation_error_code

        out["errorCode"] = aws_sdk_iot.types.sbom_validation_error_code.serialize_json(
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
        import aws_sdk_iot.types.sbom_validation_result

        out["validation_result"] = (
            aws_sdk_iot.types.sbom_validation_result.deserialize_json(
                data["validationResult"]
            )
        )
    if "errorCode" in data:
        import aws_sdk_iot.types.sbom_validation_error_code

        out["error_code"] = (
            aws_sdk_iot.types.sbom_validation_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out

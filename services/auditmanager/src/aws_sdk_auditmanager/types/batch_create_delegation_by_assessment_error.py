"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchCreateDelegationByAssessmentError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.create_delegation_request
    import aws_sdk_auditmanager.types.error_code
    import aws_sdk_auditmanager.types.error_message


class BatchCreateDelegationByAssessmentError(TypedDict, closed=True):
    create_delegation_request: NotRequired[
        "aws_sdk_auditmanager.types.create_delegation_request.CreateDelegationRequest"
    ]
    """<p> The API request to batch create delegations in Audit Manager. </p>"""
    error_code: NotRequired["aws_sdk_auditmanager.types.error_code.ErrorCode"]
    """<p> The error code that the <code>BatchCreateDelegationByAssessment</code> API returned. </p>"""
    error_message: NotRequired["aws_sdk_auditmanager.types.error_message.ErrorMessage"]
    """<p> The error message that the <code>BatchCreateDelegationByAssessment</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDelegationByAssessmentError) -> dict:
    out: dict = {}
    if "create_delegation_request" in value:
        import aws_sdk_auditmanager.types.create_delegation_request

        out["createDelegationRequest"] = (
            aws_sdk_auditmanager.types.create_delegation_request.serialize_json(
                value["create_delegation_request"]
            )
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchCreateDelegationByAssessmentError:
    out: BatchCreateDelegationByAssessmentError = {}  # type: ignore[typeddict-item]
    if "createDelegationRequest" in data:
        import aws_sdk_auditmanager.types.create_delegation_request

        out["create_delegation_request"] = (
            aws_sdk_auditmanager.types.create_delegation_request.deserialize_json(
                data["createDelegationRequest"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out

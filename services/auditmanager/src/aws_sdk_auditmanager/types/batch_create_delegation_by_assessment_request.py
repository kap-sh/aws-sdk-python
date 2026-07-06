"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchCreateDelegationByAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.create_delegation_requests
    import aws_sdk_auditmanager.types.uuid


class BatchCreateDelegationByAssessmentRequest(TypedDict, closed=True):
    create_delegation_requests: (
        "aws_sdk_auditmanager.types.create_delegation_requests.CreateDelegationRequests"
    )
    """<p> The API request to batch create delegations in Audit Manager. </p>"""
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDelegationByAssessmentRequest) -> dict:
    out: dict = {}
    import aws_sdk_auditmanager.types.create_delegation_requests

    out["createDelegationRequests"] = (
        aws_sdk_auditmanager.types.create_delegation_requests.serialize_json(
            value["create_delegation_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateDelegationByAssessmentRequest:
    out: BatchCreateDelegationByAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "createDelegationRequests" in data:
        import aws_sdk_auditmanager.types.create_delegation_requests

        out["create_delegation_requests"] = (
            aws_sdk_auditmanager.types.create_delegation_requests.deserialize_json(
                data["createDelegationRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateDelegationByAssessmentRequest.create_delegation_requests required"
        )
    return out

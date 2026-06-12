"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDeleteDelegationByAssessmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.delegation_ids
    import aws_sdk_auditmanager.types.uuid


class BatchDeleteDelegationByAssessmentRequest(TypedDict):
    delegation_ids: "aws_sdk_auditmanager.types.delegation_ids.DelegationIds"
    """<p> The identifiers for the delegations. </p>"""
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDelegationByAssessmentRequest) -> dict:
    out: dict = {}
    import aws_sdk_auditmanager.types.delegation_ids

    out["delegationIds"] = aws_sdk_auditmanager.types.delegation_ids.serialize_json(
        value["delegation_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDelegationByAssessmentRequest:
    out: BatchDeleteDelegationByAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "delegationIds" in data:
        import aws_sdk_auditmanager.types.delegation_ids

        out["delegation_ids"] = (
            aws_sdk_auditmanager.types.delegation_ids.deserialize_json(
                data["delegationIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteDelegationByAssessmentRequest.delegation_ids required"
        )
    return out

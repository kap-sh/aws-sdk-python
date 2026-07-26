"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ReasonCode``."""

from typing import Literal, TypeAlias, cast

ReasonCode: TypeAlias = Literal[
    "InvitationAccessDenied",
    "InvitationValidationFailed",
    "EngagementAccessDenied",
    "OpportunityAccessDenied",
    "ResourceSnapshotJobAccessDenied",
    "ResourceSnapshotJobValidationFailed",
    "ResourceSnapshotJobConflict",
    "EngagementValidationFailed",
    "EngagementConflict",
    "OpportunitySubmissionFailed",
    "EngagementInvitationConflict",
    "InternalError",
    "OpportunityValidationFailed",
    "OpportunityConflict",
    "ResourceSnapshotAccessDenied",
    "ResourceSnapshotValidationFailed",
    "ResourceSnapshotConflict",
    "ServiceQuotaExceeded",
    "RequestThrottled",
    "ContextNotFound",
    "CustomerProjectContextNotPermitted",
    "DisqualifiedLeadNotPermitted",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReasonCode:
    return cast(ReasonCode, data)

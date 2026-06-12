"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_0(value: ReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReasonCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReasonCode value: {data!r}")
    return cast(ReasonCode, data)

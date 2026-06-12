"""Generated from Smithy shape ``com.amazonaws.mpa#StartApprovalTeamBaselineApproverIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.participant_id

StartApprovalTeamBaselineApproverIds: TypeAlias = list[
    "aws_sdk_mpa.types.participant_id.ParticipantId"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartApprovalTeamBaselineApproverIds) -> list:
    return list(value)


def deserialize_json(data: list) -> StartApprovalTeamBaselineApproverIds:
    return list(data)

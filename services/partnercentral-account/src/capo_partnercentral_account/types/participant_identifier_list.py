"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ParticipantIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.participant_identifier

ParticipantIdentifierList: TypeAlias = list[
    "capo_partnercentral_account.types.participant_identifier.ParticipantIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParticipantIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ParticipantIdentifierList:
    return list(data)

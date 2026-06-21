"""Generated from Smithy shape ``com.amazonaws.connect#DisconnectOnCustomerExitParticipantType``."""

from typing import Literal, TypeAlias, cast

DisconnectOnCustomerExitParticipantType: TypeAlias = Literal["AGENT",]


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectOnCustomerExitParticipantType) -> str:
    return value


def deserialize_json(data: str) -> DisconnectOnCustomerExitParticipantType:
    return cast(DisconnectOnCustomerExitParticipantType, data)

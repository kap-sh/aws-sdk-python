"""Generated from Smithy shape ``com.amazonaws.connect#DisconnectOnCustomerExitParticipantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DisconnectOnCustomerExitParticipantType: TypeAlias = Literal["AGENT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AGENT",))


def serialize_json(value: DisconnectOnCustomerExitParticipantType) -> str:
    return value


def deserialize_json(data: str) -> DisconnectOnCustomerExitParticipantType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DisconnectOnCustomerExitParticipantType value: {data!r}"
        )
    return cast(DisconnectOnCustomerExitParticipantType, data)

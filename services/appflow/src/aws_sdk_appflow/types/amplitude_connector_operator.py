"""Generated from Smithy shape ``com.amazonaws.appflow#AmplitudeConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

AmplitudeConnectorOperator: TypeAlias = Literal["BETWEEN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BETWEEN",))


def serialize_json(value: AmplitudeConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> AmplitudeConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AmplitudeConnectorOperator value: {data!r}"
        )
    return cast(AmplitudeConnectorOperator, data)

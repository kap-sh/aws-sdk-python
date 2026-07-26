"""Generated from Smithy shape ``com.amazonaws.appflow#AmplitudeConnectorOperator``."""

from typing import Literal, TypeAlias, cast

AmplitudeConnectorOperator: TypeAlias = Literal["BETWEEN",]


# --- restJson1 ser/de ---
def serialize_json(value: AmplitudeConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> AmplitudeConnectorOperator:
    return cast(AmplitudeConnectorOperator, data)

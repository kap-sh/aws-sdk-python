"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAribCaptionsPidControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Arib Captions Pid Control"""
M2tsAribCaptionsPidControl: TypeAlias = Literal[
    "AUTO",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "USE_CONFIGURED",
    )
)


def serialize_json(value: M2tsAribCaptionsPidControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsAribCaptionsPidControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown M2tsAribCaptionsPidControl value: {data!r}"
        )
    return cast(M2tsAribCaptionsPidControl, data)

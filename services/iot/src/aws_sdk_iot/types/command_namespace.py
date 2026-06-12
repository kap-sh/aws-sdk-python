"""Generated from Smithy shape ``com.amazonaws.iot#CommandNamespace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CommandNamespace: TypeAlias = Literal[
    "AWS-IoT",
    "AWS-IoT-FleetWise",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS-IoT",
        "AWS-IoT-FleetWise",
    )
)


def serialize_json(value: CommandNamespace) -> str:
    return value


def deserialize_json(data: str) -> CommandNamespace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandNamespace value: {data!r}")
    return cast(CommandNamespace, data)

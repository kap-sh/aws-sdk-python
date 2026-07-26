"""Generated from Smithy shape ``com.amazonaws.iot#CommandNamespace``."""

from typing import Literal, TypeAlias, cast

CommandNamespace: TypeAlias = Literal[
    "AWS-IoT",
    "AWS-IoT-FleetWise",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandNamespace) -> str:
    return value


def deserialize_json(data: str) -> CommandNamespace:
    return cast(CommandNamespace, data)

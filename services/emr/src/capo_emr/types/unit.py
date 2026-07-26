"""Generated from Smithy shape ``com.amazonaws.emr#Unit``."""

from typing import Literal, TypeAlias, cast

Unit: TypeAlias = Literal[
    "NONE",
    "SECONDS",
    "MICRO_SECONDS",
    "MILLI_SECONDS",
    "BYTES",
    "KILO_BYTES",
    "MEGA_BYTES",
    "GIGA_BYTES",
    "TERA_BYTES",
    "BITS",
    "KILO_BITS",
    "MEGA_BITS",
    "GIGA_BITS",
    "TERA_BITS",
    "PERCENT",
    "COUNT",
    "BYTES_PER_SECOND",
    "KILO_BYTES_PER_SECOND",
    "MEGA_BYTES_PER_SECOND",
    "GIGA_BYTES_PER_SECOND",
    "TERA_BYTES_PER_SECOND",
    "BITS_PER_SECOND",
    "KILO_BITS_PER_SECOND",
    "MEGA_BITS_PER_SECOND",
    "GIGA_BITS_PER_SECOND",
    "TERA_BITS_PER_SECOND",
    "COUNT_PER_SECOND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Unit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Unit:
    return cast(Unit, data)

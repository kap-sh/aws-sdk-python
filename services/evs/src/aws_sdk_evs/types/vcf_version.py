"""Generated from Smithy shape ``com.amazonaws.evs#VcfVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

VcfVersion: TypeAlias = Literal[
    "VCF-5.2.1",
    "VCF-5.2.2",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VCF-5.2.1",
        "VCF-5.2.2",
    )
)


def serialize_aws_json_1_0(value: VcfVersion) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VcfVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VcfVersion value: {data!r}")
    return cast(VcfVersion, data)

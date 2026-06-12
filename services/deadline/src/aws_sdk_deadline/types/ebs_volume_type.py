"""Generated from Smithy shape ``com.amazonaws.deadline#EbsVolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

"""<p>The EBS volume type.</p>"""
EbsVolumeType: TypeAlias = Literal["gp3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("gp3",))


def serialize_json(value: EbsVolumeType) -> str:
    return value


def deserialize_json(data: str) -> EbsVolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EbsVolumeType value: {data!r}")
    return cast(EbsVolumeType, data)

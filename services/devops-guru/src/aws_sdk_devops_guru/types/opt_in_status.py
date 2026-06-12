"""Generated from Smithy shape ``com.amazonaws.devopsguru#OptInStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

"""<p> Specifies if DevOps Guru is enabled to create an Amazon Web Services Systems Manager OpsItem for each created insight. </p>"""
OptInStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: OptInStatus) -> str:
    return value


def deserialize_json(data: str) -> OptInStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptInStatus value: {data!r}")
    return cast(OptInStatus, data)

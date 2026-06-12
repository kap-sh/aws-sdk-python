"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#Capability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_serverlessapplicationrepository.errors import DeserializationError

"""<p>Values that must be specified in order to deploy some applications.</p>"""
Capability: TypeAlias = Literal[
    "CAPABILITY_IAM",
    "CAPABILITY_NAMED_IAM",
    "CAPABILITY_AUTO_EXPAND",
    "CAPABILITY_RESOURCE_POLICY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAPABILITY_IAM",
        "CAPABILITY_NAMED_IAM",
        "CAPABILITY_AUTO_EXPAND",
        "CAPABILITY_RESOURCE_POLICY",
    )
)


def serialize_json(value: Capability) -> str:
    return value


def deserialize_json(data: str) -> Capability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Capability value: {data!r}")
    return cast(Capability, data)

"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Verification status of a target domain.</p>"""
TargetDomainStatus: TypeAlias = Literal[
    "PENDING",
    "VERIFIED",
    "FAILED",
    "UNREACHABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "VERIFIED",
        "FAILED",
        "UNREACHABLE",
    )
)


def serialize_json(value: TargetDomainStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetDomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetDomainStatus value: {data!r}")
    return cast(TargetDomainStatus, data)

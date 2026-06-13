"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeRemediationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Strategy for automated code remediation.</p>"""
CodeRemediationStrategy: TypeAlias = Literal[
    "AUTOMATIC",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "DISABLED",
    )
)


def serialize_json(value: CodeRemediationStrategy) -> str:
    return value


def deserialize_json(data: str) -> CodeRemediationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeRemediationStrategy value: {data!r}")
    return cast(CodeRemediationStrategy, data)

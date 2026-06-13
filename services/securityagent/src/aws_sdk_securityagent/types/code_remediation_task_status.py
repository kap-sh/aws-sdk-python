"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeRemediationTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Code remediation task status.</p>"""
CodeRemediationTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: CodeRemediationTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeRemediationTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeRemediationTaskStatus value: {data!r}")
    return cast(CodeRemediationTaskStatus, data)

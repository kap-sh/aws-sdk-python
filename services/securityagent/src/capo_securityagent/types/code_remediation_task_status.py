"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeRemediationTaskStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Code remediation task status.</p>"""
CodeRemediationTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeRemediationTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeRemediationTaskStatus:
    return cast(CodeRemediationTaskStatus, data)

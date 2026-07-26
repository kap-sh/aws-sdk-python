"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeRemediationStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>Strategy for automated code remediation.</p>"""
CodeRemediationStrategy: TypeAlias = Literal[
    "AUTOMATIC",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeRemediationStrategy) -> str:
    return value


def deserialize_json(data: str) -> CodeRemediationStrategy:
    return cast(CodeRemediationStrategy, data)

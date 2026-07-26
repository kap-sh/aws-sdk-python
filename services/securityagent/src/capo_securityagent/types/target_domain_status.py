"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomainStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Verification status of a target domain.</p>"""
TargetDomainStatus: TypeAlias = Literal[
    "PENDING",
    "VERIFIED",
    "FAILED",
    "UNREACHABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetDomainStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetDomainStatus:
    return cast(TargetDomainStatus, data)

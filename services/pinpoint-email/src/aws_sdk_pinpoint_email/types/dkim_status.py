"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DkimStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint_email.errors import DeserializationError

"""<p>The DKIM authentication status of the identity. The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – The DKIM verification process was initiated, and Amazon Pinpoint is still waiting for the required CNAME records to appear in the DNS configuration for the domain.</p> </li> <li> <p> <code>SUCCESS</code> – The DKIM authentication process completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The DKIM authentication process failed. This can happen when Amazon Pinpoint fails to find the required CNAME records in the DNS configuration of the domain.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue is preventing Amazon Pinpoint from determining the DKIM authentication status of the domain.</p> </li> <li> <p> <code>NOT_STARTED</code> – The DKIM verification process hasn't been initiated for the domain.</p> </li> </ul>"""
DkimStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
    "TEMPORARY_FAILURE",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESS",
        "FAILED",
        "TEMPORARY_FAILURE",
        "NOT_STARTED",
    )
)


def serialize_json(value: DkimStatus) -> str:
    return value


def deserialize_json(data: str) -> DkimStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DkimStatus value: {data!r}")
    return cast(DkimStatus, data)

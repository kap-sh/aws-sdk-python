"""Generated from Smithy shape ``com.amazonaws.sesv2#DkimStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The DKIM authentication status of the identity. The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – The verification process was initiated, but Amazon SES hasn't yet detected the DKIM records in the DNS configuration for the domain.</p> </li> <li> <p> <code>SUCCESS</code> – The verification process completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The verification process failed. This typically occurs when Amazon SES fails to find the DKIM records in the DNS configuration of the domain.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue is preventing Amazon SES from determining the DKIM authentication status of the domain.</p> </li> <li> <p> <code>NOT_STARTED</code> – The DKIM verification process hasn't been initiated for the domain.</p> </li> </ul>"""
DkimStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
    "TEMPORARY_FAILURE",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DkimStatus) -> str:
    return value


def deserialize_json(data: str) -> DkimStatus:
    return cast(DkimStatus, data)

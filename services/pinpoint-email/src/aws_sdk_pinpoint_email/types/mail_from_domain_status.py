"""Generated from Smithy shape ``com.amazonaws.pinpointemail#MailFromDomainStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the MAIL FROM domain. This status can have the following values:</p> <ul> <li> <p> <code>PENDING</code> – Amazon Pinpoint hasn't started searching for the MX record yet.</p> </li> <li> <p> <code>SUCCESS</code> – Amazon Pinpoint detected the required MX record for the MAIL FROM domain.</p> </li> <li> <p> <code>FAILED</code> – Amazon Pinpoint can't find the required MX record, or the record no longer exists.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue occurred, which prevented Amazon Pinpoint from determining the status of the MAIL FROM domain.</p> </li> </ul>"""
MailFromDomainStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
    "TEMPORARY_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MailFromDomainStatus) -> str:
    return value


def deserialize_json(data: str) -> MailFromDomainStatus:
    return cast(MailFromDomainStatus, data)

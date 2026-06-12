"""Generated from Smithy shape ``com.amazonaws.sesv2#MailFromDomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The status of the MAIL FROM domain. This status can have the following values:</p> <ul> <li> <p> <code>PENDING</code> – Amazon SES hasn't started searching for the MX record yet.</p> </li> <li> <p> <code>SUCCESS</code> – Amazon SES detected the required MX record for the MAIL FROM domain.</p> </li> <li> <p> <code>FAILED</code> – Amazon SES can't find the required MX record, or the record no longer exists.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue occurred, which prevented Amazon SES from determining the status of the MAIL FROM domain.</p> </li> </ul>"""
MailFromDomainStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
    "TEMPORARY_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESS",
        "FAILED",
        "TEMPORARY_FAILURE",
    )
)


def serialize_json(value: MailFromDomainStatus) -> str:
    return value


def deserialize_json(data: str) -> MailFromDomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MailFromDomainStatus value: {data!r}")
    return cast(MailFromDomainStatus, data)

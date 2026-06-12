"""Generated from Smithy shape ``com.amazonaws.pinpointemail#BehaviorOnMxFailure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint_email.errors import DeserializationError

"""<p>The action that you want Amazon Pinpoint to take if it can't read the required MX record for a custom MAIL FROM domain. When you set this value to <code>UseDefaultValue</code>, Amazon Pinpoint uses <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>RejectMessage</code>, Amazon Pinpoint returns a <code>MailFromDomainNotVerified</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>"""
BehaviorOnMxFailure: TypeAlias = Literal[
    "USE_DEFAULT_VALUE",
    "REJECT_MESSAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USE_DEFAULT_VALUE",
        "REJECT_MESSAGE",
    )
)


def serialize_json(value: BehaviorOnMxFailure) -> str:
    return value


def deserialize_json(data: str) -> BehaviorOnMxFailure:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BehaviorOnMxFailure value: {data!r}")
    return cast(BehaviorOnMxFailure, data)

"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailAddressInsightsConfidenceVerdict``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The confidence level of SES that the email address meets the validation criteria:</p> <ul> <li> <p> <code>LOW</code> - Weak or no indication of the speciﬁc check (e.g., LOW for IsRoleAddress means the email is less likely to be a role-based address).</p> </li> <li> <p> <code>MEDIUM</code> - Moderate indication of the speciﬁc check (e.g., MEDIUM for IsDisposable means the email might be a disposable address).</p> </li> <li> <p> <code>HIGH</code> - Strong indication of the speciﬁc check (e.g., HIGH for IsRandomInput means the email is very likely randomly generated).</p> </li> </ul>"""
EmailAddressInsightsConfidenceVerdict: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: EmailAddressInsightsConfidenceVerdict) -> str:
    return value


def deserialize_json(data: str) -> EmailAddressInsightsConfidenceVerdict:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EmailAddressInsightsConfidenceVerdict value: {data!r}"
        )
    return cast(EmailAddressInsightsConfidenceVerdict, data)

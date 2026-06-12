"""Generated from Smithy shape ``com.amazonaws.mpa#MfaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

"""<p>The type of MFA device used by the approver</p> <ul> <li> <p> <code>EMAIL_OTP</code>: The approver will receive emailed one-time passwords to their primary email</p> </li> </ul>"""
MfaType: TypeAlias = Literal["EMAIL_OTP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EMAIL_OTP",))


def serialize_json(value: MfaType) -> str:
    return value


def deserialize_json(data: str) -> MfaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MfaType value: {data!r}")
    return cast(MfaType, data)

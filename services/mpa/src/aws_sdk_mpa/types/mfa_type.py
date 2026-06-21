"""Generated from Smithy shape ``com.amazonaws.mpa#MfaType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of MFA device used by the approver</p> <ul> <li> <p> <code>EMAIL_OTP</code>: The approver will receive emailed one-time passwords to their primary email</p> </li> </ul>"""
MfaType: TypeAlias = Literal["EMAIL_OTP",]


# --- restJson1 ser/de ---
def serialize_json(value: MfaType) -> str:
    return value


def deserialize_json(data: str) -> MfaType:
    return cast(MfaType, data)

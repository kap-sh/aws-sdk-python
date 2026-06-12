"""Generated from Smithy shape ``com.amazonaws.mpa#AdditionalSecurityRequirement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

"""<p>Additional security requirements applied to a session or invitation</p> <ul> <li> <p> <code>APPROVER_VERIFICATION_REQUIRED</code>: Approvers will be required to perform an MFA challenge to vote</p> </li> </ul>"""
AdditionalSecurityRequirement: TypeAlias = Literal["APPROVER_VERIFICATION_REQUIRED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("APPROVER_VERIFICATION_REQUIRED",))


def serialize_json(value: AdditionalSecurityRequirement) -> str:
    return value


def deserialize_json(data: str) -> AdditionalSecurityRequirement:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdditionalSecurityRequirement value: {data!r}"
        )
    return cast(AdditionalSecurityRequirement, data)

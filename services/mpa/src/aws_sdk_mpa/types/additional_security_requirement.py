"""Generated from Smithy shape ``com.amazonaws.mpa#AdditionalSecurityRequirement``."""

from typing import Literal, TypeAlias, cast

"""<p>Additional security requirements applied to a session or invitation</p> <ul> <li> <p> <code>APPROVER_VERIFICATION_REQUIRED</code>: Approvers will be required to perform an MFA challenge to vote</p> </li> </ul>"""
AdditionalSecurityRequirement: TypeAlias = Literal["APPROVER_VERIFICATION_REQUIRED",]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalSecurityRequirement) -> str:
    return value


def deserialize_json(data: str) -> AdditionalSecurityRequirement:
    return cast(AdditionalSecurityRequirement, data)

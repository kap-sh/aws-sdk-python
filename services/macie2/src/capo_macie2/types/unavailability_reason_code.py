"""Generated from Smithy shape ``com.amazonaws.macie2#UnavailabilityReasonCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies why occurrences of sensitive data can't be retrieved for a finding. Possible values are:</p>"""
UnavailabilityReasonCode: TypeAlias = Literal[
    "OBJECT_EXCEEDS_SIZE_QUOTA",
    "UNSUPPORTED_OBJECT_TYPE",
    "UNSUPPORTED_FINDING_TYPE",
    "INVALID_CLASSIFICATION_RESULT",
    "OBJECT_UNAVAILABLE",
    "ACCOUNT_NOT_IN_ORGANIZATION",
    "MISSING_GET_MEMBER_PERMISSION",
    "ROLE_TOO_PERMISSIVE",
    "MEMBER_ROLE_TOO_PERMISSIVE",
    "INVALID_RESULT_SIGNATURE",
    "RESULT_NOT_SIGNED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UnavailabilityReasonCode) -> str:
    return value


def deserialize_json(data: str) -> UnavailabilityReasonCode:
    return cast(UnavailabilityReasonCode, data)

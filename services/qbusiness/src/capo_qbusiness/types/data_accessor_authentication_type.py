"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorAuthenticationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of authentication mechanism used by the data accessor.</p>"""
DataAccessorAuthenticationType: TypeAlias = Literal[
    "AWS_IAM_IDC_TTI",
    "AWS_IAM_IDC_AUTH_CODE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessorAuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> DataAccessorAuthenticationType:
    return cast(DataAccessorAuthenticationType, data)

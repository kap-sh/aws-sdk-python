"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

"""<p>The type of authentication mechanism used by the data accessor.</p>"""
DataAccessorAuthenticationType: TypeAlias = Literal[
    "AWS_IAM_IDC_TTI",
    "AWS_IAM_IDC_AUTH_CODE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_IAM_IDC_TTI",
        "AWS_IAM_IDC_AUTH_CODE",
    )
)


def serialize_json(value: DataAccessorAuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> DataAccessorAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataAccessorAuthenticationType value: {data!r}"
        )
    return cast(DataAccessorAuthenticationType, data)

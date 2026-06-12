"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PrincipalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>Specifies the type of AWS account permitted to manage VPC endpoints.: <ul> <li>AWS_ACCOUNT: Indicates that the account is owned by an AWS user.</li> <li>AWS_SERVICE: Indicates the the account is owned by an AWS service.</li> </ul> </p>"""
PrincipalType: TypeAlias = Literal[
    "AWS_ACCOUNT",
    "AWS_SERVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_ACCOUNT",
        "AWS_SERVICE",
    )
)


def serialize_json(value: PrincipalType) -> str:
    return value


def deserialize_json(data: str) -> PrincipalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalType value: {data!r}")
    return cast(PrincipalType, data)

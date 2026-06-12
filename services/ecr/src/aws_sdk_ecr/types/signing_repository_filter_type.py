"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRepositoryFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

"""<p>The type of filter to use when determining which repositories should have their images automatically signed.</p>"""
SigningRepositoryFilterType: TypeAlias = Literal["WILDCARD_MATCH",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WILDCARD_MATCH",))


def serialize_aws_json_1_1(value: SigningRepositoryFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningRepositoryFilterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SigningRepositoryFilterType value: {data!r}"
        )
    return cast(SigningRepositoryFilterType, data)

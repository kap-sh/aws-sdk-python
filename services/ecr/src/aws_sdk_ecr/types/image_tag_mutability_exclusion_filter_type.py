"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutabilityExclusionFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ImageTagMutabilityExclusionFilterType: TypeAlias = Literal["WILDCARD",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WILDCARD",))


def serialize_aws_json_1_1(value: ImageTagMutabilityExclusionFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageTagMutabilityExclusionFilterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ImageTagMutabilityExclusionFilterType value: {data!r}"
        )
    return cast(ImageTagMutabilityExclusionFilterType, data)

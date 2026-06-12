"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#ContentClassifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_a2i_runtime.errors import DeserializationError

ContentClassifier: TypeAlias = Literal[
    "FreeOfPersonallyIdentifiableInformation",
    "FreeOfAdultContent",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FreeOfPersonallyIdentifiableInformation",
        "FreeOfAdultContent",
    )
)


def serialize_json(value: ContentClassifier) -> str:
    return value


def deserialize_json(data: str) -> ContentClassifier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentClassifier value: {data!r}")
    return cast(ContentClassifier, data)

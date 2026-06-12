"""Generated from Smithy shape ``com.amazonaws.textract#ContentClassifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

ContentClassifier: TypeAlias = Literal[
    "FreeOfPersonallyIdentifiableInformation",
    "FreeOfAdultContent",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FreeOfPersonallyIdentifiableInformation",
        "FreeOfAdultContent",
    )
)


def serialize_aws_json_1_1(value: ContentClassifier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentClassifier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentClassifier value: {data!r}")
    return cast(ContentClassifier, data)

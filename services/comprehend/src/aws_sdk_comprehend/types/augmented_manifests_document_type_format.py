"""Generated from Smithy shape ``com.amazonaws.comprehend#AugmentedManifestsDocumentTypeFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

AugmentedManifestsDocumentTypeFormat: TypeAlias = Literal[
    "PLAIN_TEXT_DOCUMENT",
    "SEMI_STRUCTURED_DOCUMENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLAIN_TEXT_DOCUMENT",
        "SEMI_STRUCTURED_DOCUMENT",
    )
)


def serialize_aws_json_1_1(value: AugmentedManifestsDocumentTypeFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AugmentedManifestsDocumentTypeFormat:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AugmentedManifestsDocumentTypeFormat value: {data!r}"
        )
    return cast(AugmentedManifestsDocumentTypeFormat, data)

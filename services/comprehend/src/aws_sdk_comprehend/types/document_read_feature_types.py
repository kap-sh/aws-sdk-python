"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentReadFeatureTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

"""<p>TABLES or FORMS</p>"""
DocumentReadFeatureTypes: TypeAlias = Literal[
    "TABLES",
    "FORMS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TABLES",
        "FORMS",
    )
)


def serialize_aws_json_1_1(value: DocumentReadFeatureTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReadFeatureTypes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentReadFeatureTypes value: {data!r}")
    return cast(DocumentReadFeatureTypes, data)

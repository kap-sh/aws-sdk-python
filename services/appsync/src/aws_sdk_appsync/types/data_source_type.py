"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

DataSourceType: TypeAlias = Literal[
    "AWS_LAMBDA",
    "AMAZON_DYNAMODB",
    "AMAZON_ELASTICSEARCH",
    "NONE",
    "HTTP",
    "RELATIONAL_DATABASE",
    "AMAZON_OPENSEARCH_SERVICE",
    "AMAZON_EVENTBRIDGE",
    "AMAZON_BEDROCK_RUNTIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_LAMBDA",
        "AMAZON_DYNAMODB",
        "AMAZON_ELASTICSEARCH",
        "NONE",
        "HTTP",
        "RELATIONAL_DATABASE",
        "AMAZON_OPENSEARCH_SERVICE",
        "AMAZON_EVENTBRIDGE",
        "AMAZON_BEDROCK_RUNTIME",
    )
)


def serialize_json(value: DataSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceType value: {data!r}")
    return cast(DataSourceType, data)

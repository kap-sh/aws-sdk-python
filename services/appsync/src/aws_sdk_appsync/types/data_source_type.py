"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DataSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceType:
    return cast(DataSourceType, data)

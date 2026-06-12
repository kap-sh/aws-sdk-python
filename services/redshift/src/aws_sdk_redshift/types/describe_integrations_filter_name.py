"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeIntegrationsFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

DescribeIntegrationsFilterName: TypeAlias = Literal[
    "integration-arn",
    "source-arn",
    "source-types",
    "status",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "integration-arn",
        "source-arn",
        "source-types",
        "status",
    )
)


def to_query_text(value: DescribeIntegrationsFilterName) -> str:
    return value


def from_query_text(text: str) -> DescribeIntegrationsFilterName:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown DescribeIntegrationsFilterName value: {text!r}"
        )
    return cast(DescribeIntegrationsFilterName, text)


def serialize_query(
    value: DescribeIntegrationsFilterName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DescribeIntegrationsFilterName:
    return from_query_text(el.text or "")

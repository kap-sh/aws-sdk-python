"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationOptionValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

ConfigurationOptionValueType: TypeAlias = Literal[
    "Scalar",
    "List",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Scalar",
        "List",
    )
)


def to_query_text(value: ConfigurationOptionValueType) -> str:
    return value


def from_query_text(text: str) -> ConfigurationOptionValueType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurationOptionValueType value: {text!r}"
        )
    return cast(ConfigurationOptionValueType, text)


def serialize_query(
    value: ConfigurationOptionValueType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ConfigurationOptionValueType:
    return from_query_text(el.text or "")

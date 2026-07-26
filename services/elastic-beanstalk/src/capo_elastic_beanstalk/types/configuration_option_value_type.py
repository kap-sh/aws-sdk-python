"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationOptionValueType``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

ConfigurationOptionValueType: TypeAlias = Literal[
    "Scalar",
    "List",
]


# --- awsQuery ser/de ---
def to_query_text(value: ConfigurationOptionValueType) -> str:
    return value


def from_query_text(text: str) -> ConfigurationOptionValueType:
    return cast(ConfigurationOptionValueType, text)


def serialize_query(
    value: ConfigurationOptionValueType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ConfigurationOptionValueType:
    return from_query_text(el.text or "")

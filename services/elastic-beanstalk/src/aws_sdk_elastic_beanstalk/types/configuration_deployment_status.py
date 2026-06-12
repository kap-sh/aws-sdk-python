"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

ConfigurationDeploymentStatus: TypeAlias = Literal[
    "deployed",
    "pending",
    "failed",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "deployed",
        "pending",
        "failed",
    )
)


def to_query_text(value: ConfigurationDeploymentStatus) -> str:
    return value


def from_query_text(text: str) -> ConfigurationDeploymentStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurationDeploymentStatus value: {text!r}"
        )
    return cast(ConfigurationDeploymentStatus, text)


def serialize_query(
    value: ConfigurationDeploymentStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ConfigurationDeploymentStatus:
    return from_query_text(el.text or "")

"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationVersionStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

ApplicationVersionStatus: TypeAlias = Literal[
    "Processed",
    "Unprocessed",
    "Failed",
    "Processing",
    "Building",
]


# --- awsQuery ser/de ---
def to_query_text(value: ApplicationVersionStatus) -> str:
    return value


def from_query_text(text: str) -> ApplicationVersionStatus:
    return cast(ApplicationVersionStatus, text)


def serialize_query(
    value: ApplicationVersionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ApplicationVersionStatus:
    return from_query_text(el.text or "")

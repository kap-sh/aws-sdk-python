"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ActionStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

ActionStatus: TypeAlias = Literal[
    "Scheduled",
    "Pending",
    "Running",
    "Unknown",
]


# --- awsQuery ser/de ---
def to_query_text(value: ActionStatus) -> str:
    return value


def from_query_text(text: str) -> ActionStatus:
    return cast(ActionStatus, text)


def serialize_query(
    value: ActionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActionStatus:
    return from_query_text(el.text or "")

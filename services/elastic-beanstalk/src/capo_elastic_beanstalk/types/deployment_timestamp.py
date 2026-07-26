"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeploymentTimestamp``."""

import datetime
from typing import TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

DeploymentTimestamp: TypeAlias = datetime.datetime


# --- awsQuery ser/de ---
def to_query_text(value: DeploymentTimestamp) -> str:
    return value.isoformat()


def from_query_text(text: str) -> DeploymentTimestamp:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: DeploymentTimestamp, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeploymentTimestamp:
    return from_query_text(el.text or "")

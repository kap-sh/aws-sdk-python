"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

ElasticGpuStatus: TypeAlias = Literal[
    "OK",
    "IMPAIRED",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ElasticGpuStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> ElasticGpuStatus:
    return cast(ElasticGpuStatus, text)


def serialize_ec2_query(
    value: ElasticGpuStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ElasticGpuStatus:
    return from_ec2_query_text(el.text or "")

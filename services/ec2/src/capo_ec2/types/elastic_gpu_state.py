"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ElasticGpuState: TypeAlias = Literal["ATTACHED",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ElasticGpuState) -> str:
    return value


def from_ec2_query_text(text: str) -> ElasticGpuState:
    return cast(ElasticGpuState, text)


def serialize_ec2_query(
    value: ElasticGpuState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ElasticGpuState:
    return from_ec2_query_text(el.text or "")

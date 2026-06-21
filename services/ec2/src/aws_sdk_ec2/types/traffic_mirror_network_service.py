"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorNetworkService``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TrafficMirrorNetworkService: TypeAlias = Literal["amazon-dns",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TrafficMirrorNetworkService) -> str:
    return value


def from_ec2_query_text(text: str) -> TrafficMirrorNetworkService:
    return cast(TrafficMirrorNetworkService, text)


def serialize_ec2_query(
    value: TrafficMirrorNetworkService, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TrafficMirrorNetworkService:
    return from_ec2_query_text(el.text or "")

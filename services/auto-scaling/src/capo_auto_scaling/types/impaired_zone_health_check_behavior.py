"""Generated from Smithy shape ``com.amazonaws.autoscaling#ImpairedZoneHealthCheckBehavior``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

ImpairedZoneHealthCheckBehavior: TypeAlias = Literal[
    "ReplaceUnhealthy",
    "IgnoreUnhealthy",
]


# --- awsQuery ser/de ---
def to_query_text(value: ImpairedZoneHealthCheckBehavior) -> str:
    return value


def from_query_text(text: str) -> ImpairedZoneHealthCheckBehavior:
    return cast(ImpairedZoneHealthCheckBehavior, text)


def serialize_query(
    value: ImpairedZoneHealthCheckBehavior, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ImpairedZoneHealthCheckBehavior:
    return from_query_text(el.text or "")

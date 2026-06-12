"""Generated from Smithy shape ``com.amazonaws.autoscaling#DetachTrafficSourcesResultType``."""

from typing import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class DetachTrafficSourcesResultType(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DetachTrafficSourcesResultType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DetachTrafficSourcesResultType:
    out: DetachTrafficSourcesResultType = {}  # type: ignore[typeddict-item]
    return out

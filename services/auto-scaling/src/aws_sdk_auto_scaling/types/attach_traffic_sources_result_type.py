"""Generated from Smithy shape ``com.amazonaws.autoscaling#AttachTrafficSourcesResultType``."""

from typing import TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element


class AttachTrafficSourcesResultType(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachTrafficSourcesResultType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> AttachTrafficSourcesResultType:
    out: AttachTrafficSourcesResultType = {}  # type: ignore[typeddict-item]
    return out

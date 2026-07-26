"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceSignalStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ResourceSignalStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILURE",
]


# --- awsQuery ser/de ---
def to_query_text(value: ResourceSignalStatus) -> str:
    return value


def from_query_text(text: str) -> ResourceSignalStatus:
    return cast(ResourceSignalStatus, text)


def serialize_query(
    value: ResourceSignalStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ResourceSignalStatus:
    return from_query_text(el.text or "")

"""Generated from Smithy shape ``com.amazonaws.rds#CustomEngineVersionStatus``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

CustomEngineVersionStatus: TypeAlias = Literal[
    "available",
    "inactive",
    "inactive-except-restore",
]


# --- awsQuery ser/de ---
def to_query_text(value: CustomEngineVersionStatus) -> str:
    return value


def from_query_text(text: str) -> CustomEngineVersionStatus:
    return cast(CustomEngineVersionStatus, text)


def serialize_query(
    value: CustomEngineVersionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CustomEngineVersionStatus:
    return from_query_text(el.text or "")

"""Generated from Smithy shape ``com.amazonaws.rds#LimitlessDatabaseStatus``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

LimitlessDatabaseStatus: TypeAlias = Literal[
    "active",
    "not-in-use",
    "enabled",
    "disabled",
    "enabling",
    "disabling",
    "modifying-max-capacity",
    "error",
]


# --- awsQuery ser/de ---
def to_query_text(value: LimitlessDatabaseStatus) -> str:
    return value


def from_query_text(text: str) -> LimitlessDatabaseStatus:
    return cast(LimitlessDatabaseStatus, text)


def serialize_query(
    value: LimitlessDatabaseStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LimitlessDatabaseStatus:
    return from_query_text(el.text or "")

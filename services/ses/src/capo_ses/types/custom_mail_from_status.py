"""Generated from Smithy shape ``com.amazonaws.ses#CustomMailFromStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ses._protocol.xml import Element

CustomMailFromStatus: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failed",
    "TemporaryFailure",
]


# --- awsQuery ser/de ---
def to_query_text(value: CustomMailFromStatus) -> str:
    return value


def from_query_text(text: str) -> CustomMailFromStatus:
    return cast(CustomMailFromStatus, text)


def serialize_query(
    value: CustomMailFromStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CustomMailFromStatus:
    return from_query_text(el.text or "")

"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime

from capo_sns._protocol.xml import Element


# --- awsQuery ser/de ---
def to_query_text(value: datetime.datetime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_query_text(text: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: datetime.datetime, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> datetime.datetime:
    return from_query_text(el.text or "")

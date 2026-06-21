"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

DataShareType: TypeAlias = Literal["INTERNAL",]


# --- awsQuery ser/de ---
def to_query_text(value: DataShareType) -> str:
    return value


def from_query_text(text: str) -> DataShareType:
    return cast(DataShareType, text)


def serialize_query(
    value: DataShareType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataShareType:
    return from_query_text(el.text or "")

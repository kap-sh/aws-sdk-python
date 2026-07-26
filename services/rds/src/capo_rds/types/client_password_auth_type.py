"""Generated from Smithy shape ``com.amazonaws.rds#ClientPasswordAuthType``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

ClientPasswordAuthType: TypeAlias = Literal[
    "MYSQL_NATIVE_PASSWORD",
    "MYSQL_CACHING_SHA2_PASSWORD",
    "POSTGRES_SCRAM_SHA_256",
    "POSTGRES_MD5",
    "SQL_SERVER_AUTHENTICATION",
]


# --- awsQuery ser/de ---
def to_query_text(value: ClientPasswordAuthType) -> str:
    return value


def from_query_text(text: str) -> ClientPasswordAuthType:
    return cast(ClientPasswordAuthType, text)


def serialize_query(
    value: ClientPasswordAuthType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ClientPasswordAuthType:
    return from_query_text(el.text or "")

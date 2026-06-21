"""Generated from Smithy shape ``com.amazonaws.rds#MasterUserAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

MasterUserAuthenticationType: TypeAlias = Literal[
    "password",
    "iam-db-auth",
]


# --- awsQuery ser/de ---
def to_query_text(value: MasterUserAuthenticationType) -> str:
    return value


def from_query_text(text: str) -> MasterUserAuthenticationType:
    return cast(MasterUserAuthenticationType, text)


def serialize_query(
    value: MasterUserAuthenticationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MasterUserAuthenticationType:
    return from_query_text(el.text or "")

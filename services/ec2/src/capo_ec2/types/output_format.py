"""Generated from Smithy shape ``com.amazonaws.ec2#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

OutputFormat: TypeAlias = Literal[
    "csv",
    "parquet",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: OutputFormat) -> str:
    return value


def from_ec2_query_text(text: str) -> OutputFormat:
    return cast(OutputFormat, text)


def serialize_ec2_query(
    value: OutputFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> OutputFormat:
    return from_ec2_query_text(el.text or "")

"""Generated from Smithy shape ``com.amazonaws.s3#ParquetInput``."""

from typing import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement


class ParquetInput(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: ParquetInput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ParquetInput:
    out: ParquetInput = {}  # type: ignore[typeddict-item]
    return out

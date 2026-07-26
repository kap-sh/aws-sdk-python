"""Generated from Smithy shape ``com.amazonaws.s3#RenameSourceIfUnmodifiedSince``."""

import datetime
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http
from typing import TypeAlias

from capo_s3._protocol.xml import Element, SubElement

RenameSourceIfUnmodifiedSince: TypeAlias = datetime.datetime


# --- restXml ser/de ---
def to_xml_text(value: RenameSourceIfUnmodifiedSince) -> str:
    return _fmt_http(value, usegmt=True)


def from_xml_text(text: str) -> RenameSourceIfUnmodifiedSince:
    return _parse_http(text)


def serialize_xml(
    value: RenameSourceIfUnmodifiedSince, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RenameSourceIfUnmodifiedSince:
    return from_xml_text(el.text or "")

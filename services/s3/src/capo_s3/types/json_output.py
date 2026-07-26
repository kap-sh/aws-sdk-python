"""Generated from Smithy shape ``com.amazonaws.s3#JSONOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.record_delimiter


class JSONOutput(TypedDict, closed=True):
    record_delimiter: NotRequired["capo_s3.types.record_delimiter.RecordDelimiter"]
    r"""<p>The value used to separate individual records in the output. If no value is specified, Amazon S3 uses a newline character ('\n').</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JSONOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "record_delimiter" in value:
        SubElement(el, "RecordDelimiter").text = str(value["record_delimiter"])


def deserialize_xml(el: Element) -> JSONOutput:
    out: JSONOutput = {}  # type: ignore[typeddict-item]
    child_record_delimiter = el.find("RecordDelimiter")
    if child_record_delimiter is not None:
        out["record_delimiter"] = str(child_record_delimiter.text or "")
    return out

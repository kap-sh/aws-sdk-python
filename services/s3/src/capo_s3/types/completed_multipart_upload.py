"""Generated from Smithy shape ``com.amazonaws.s3#CompletedMultipartUpload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.completed_part_list


class CompletedMultipartUpload(TypedDict, closed=True):
    parts: NotRequired["capo_s3.types.completed_part_list.CompletedPartList"]
    """<p>Array of CompletedPart data types.</p> <p>If you do not supply a valid <code>Part</code> with your request, the service sends back an HTTP 400 response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CompletedMultipartUpload, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "parts" in value:
        import capo_s3.types.completed_part_list

        capo_s3.types.completed_part_list.serialize_xml_flat(value["parts"], el, "Part")


def deserialize_xml(el: Element) -> CompletedMultipartUpload:
    out: CompletedMultipartUpload = {}  # type: ignore[typeddict-item]
    if el.find("Part") is not None:
        import capo_s3.types.completed_part_list

        out["parts"] = capo_s3.types.completed_part_list.deserialize_xml_flat(
            el, "Part"
        )
    return out

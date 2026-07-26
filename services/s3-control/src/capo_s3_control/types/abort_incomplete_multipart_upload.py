"""Generated from Smithy shape ``com.amazonaws.s3control#AbortIncompleteMultipartUpload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.days_after_initiation


class AbortIncompleteMultipartUpload(TypedDict, closed=True):
    days_after_initiation: (
        "capo_s3_control.types.days_after_initiation.DaysAfterInitiation"
    )
    """<p>Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload to the Outposts bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AbortIncompleteMultipartUpload, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "DaysAfterInitiation").text = str(
        value.get("days_after_initiation", 0)
    )


def deserialize_xml(el: Element) -> AbortIncompleteMultipartUpload:
    out: AbortIncompleteMultipartUpload = {}  # type: ignore[typeddict-item]
    child_days_after_initiation = el.find("DaysAfterInitiation")
    if child_days_after_initiation is not None:
        out["days_after_initiation"] = int(child_days_after_initiation.text or "")
    else:
        out["days_after_initiation"] = 0
    return out

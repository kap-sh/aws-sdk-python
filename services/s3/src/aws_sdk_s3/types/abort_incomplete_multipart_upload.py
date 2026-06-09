"""Generated from Smithy shape ``com.amazonaws.s3#AbortIncompleteMultipartUpload``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.days_after_initiation


class AbortIncompleteMultipartUpload(TypedDict):
    days_after_initiation: NotRequired[
        "aws_sdk_s3.types.days_after_initiation.DaysAfterInitiation"
    ]
    """<p>Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AbortIncompleteMultipartUpload, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "days_after_initiation" in value:
        SubElement(el, "DaysAfterInitiation").text = str(value["days_after_initiation"])


def deserialize_xml(el: Element) -> AbortIncompleteMultipartUpload:
    out: AbortIncompleteMultipartUpload = {}  # type: ignore[typeddict-item]
    child_days_after_initiation = el.find("DaysAfterInitiation")
    if child_days_after_initiation is not None:
        out["days_after_initiation"] = int(child_days_after_initiation.text or "")
    return out

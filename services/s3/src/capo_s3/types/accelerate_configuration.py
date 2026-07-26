"""Generated from Smithy shape ``com.amazonaws.s3#AccelerateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_accelerate_status


class AccelerateConfiguration(TypedDict, closed=True):
    status: NotRequired["capo_s3.types.bucket_accelerate_status.BucketAccelerateStatus"]
    """<p>Specifies the transfer acceleration status of the bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AccelerateConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        import capo_s3.types.bucket_accelerate_status

        capo_s3.types.bucket_accelerate_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> AccelerateConfiguration:
    out: AccelerateConfiguration = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.bucket_accelerate_status

        out["status"] = capo_s3.types.bucket_accelerate_status.deserialize_xml(
            child_status
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.s3#AbacStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_abac_status


class AbacStatus(TypedDict):
    status: NotRequired["aws_sdk_s3.types.bucket_abac_status.BucketAbacStatus"]
    """<p>The ABAC status of the general purpose bucket. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: AbacStatus, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        import aws_sdk_s3.types.bucket_abac_status

        aws_sdk_s3.types.bucket_abac_status.serialize_xml(value["status"], el, "Status")


def deserialize_xml(el: Element) -> AbacStatus:
    out: AbacStatus = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3.types.bucket_abac_status

        out["status"] = aws_sdk_s3.types.bucket_abac_status.deserialize_xml(
            child_status
        )
    return out

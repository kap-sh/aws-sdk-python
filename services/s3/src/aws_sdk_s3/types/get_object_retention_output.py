"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectRetentionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_lock_retention


class GetObjectRetentionOutput(TypedDict):
    retention: NotRequired["aws_sdk_s3.types.object_lock_retention.ObjectLockRetention"]
    """<p>The container element for an object's retention settings.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetObjectRetentionOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "retention" in value:
        import aws_sdk_s3.types.object_lock_retention

        aws_sdk_s3.types.object_lock_retention.serialize_xml(
            value["retention"], el, "Retention"
        )


def deserialize_xml(el: Element) -> GetObjectRetentionOutput:
    out: GetObjectRetentionOutput = {}  # type: ignore[typeddict-item]
    child_retention = el.find("Retention")
    if child_retention is not None:
        import aws_sdk_s3.types.object_lock_retention

        out["retention"] = aws_sdk_s3.types.object_lock_retention.deserialize_xml(
            child_retention
        )
    return out

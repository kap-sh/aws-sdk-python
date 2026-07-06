"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketAbacOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.abac_status


class GetBucketAbacOutput(TypedDict, closed=True):
    abac_status: NotRequired["aws_sdk_s3.types.abac_status.AbacStatus"]
    """<p>The ABAC status of the general purpose bucket. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketAbacOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "abac_status" in value:
        import aws_sdk_s3.types.abac_status

        aws_sdk_s3.types.abac_status.serialize_xml(
            value["abac_status"], el, "AbacStatus"
        )


def deserialize_xml(el: Element) -> GetBucketAbacOutput:
    out: GetBucketAbacOutput = {}  # type: ignore[typeddict-item]
    child_abac_status = el.find("AbacStatus")
    if child_abac_status is not None:
        import aws_sdk_s3.types.abac_status

        out["abac_status"] = aws_sdk_s3.types.abac_status.deserialize_xml(
            child_abac_status
        )
    return out

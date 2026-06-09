"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketOwnershipControlsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.ownership_controls


class GetBucketOwnershipControlsOutput(TypedDict):
    ownership_controls: NotRequired[
        "aws_sdk_s3.types.ownership_controls.OwnershipControls"
    ]
    """<p>The <code>OwnershipControls</code> (BucketOwnerEnforced, BucketOwnerPreferred, or ObjectWriter) currently in effect for this Amazon S3 bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketOwnershipControlsOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "ownership_controls" in value:
        import aws_sdk_s3.types.ownership_controls

        aws_sdk_s3.types.ownership_controls.serialize_xml(
            value["ownership_controls"], el, "OwnershipControls"
        )


def deserialize_xml(el: Element) -> GetBucketOwnershipControlsOutput:
    out: GetBucketOwnershipControlsOutput = {}  # type: ignore[typeddict-item]
    child_ownership_controls = el.find("OwnershipControls")
    if child_ownership_controls is not None:
        import aws_sdk_s3.types.ownership_controls

        out["ownership_controls"] = aws_sdk_s3.types.ownership_controls.deserialize_xml(
            child_ownership_controls
        )
    return out

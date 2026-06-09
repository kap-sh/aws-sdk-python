"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketAccelerateConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_accelerate_status
    import aws_sdk_s3.types.request_charged


class GetBucketAccelerateConfigurationOutput(TypedDict):
    status: NotRequired[
        "aws_sdk_s3.types.bucket_accelerate_status.BucketAccelerateStatus"
    ]
    """<p>The accelerate configuration of the bucket.</p>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketAccelerateConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        import aws_sdk_s3.types.bucket_accelerate_status

        aws_sdk_s3.types.bucket_accelerate_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> GetBucketAccelerateConfigurationOutput:
    out: GetBucketAccelerateConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3.types.bucket_accelerate_status

        out["status"] = aws_sdk_s3.types.bucket_accelerate_status.deserialize_xml(
            child_status
        )
    return out

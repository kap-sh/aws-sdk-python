"""Generated from Smithy shape ``com.amazonaws.s3#RestoreObjectOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.request_charged
    import aws_sdk_s3.types.restore_output_path


class RestoreObjectOutput(TypedDict):
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]
    restore_output_path: NotRequired[
        "aws_sdk_s3.types.restore_output_path.RestoreOutputPath"
    ]
    """<p>Indicates the path in the provided S3 output location where Select results will be restored to.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RestoreObjectOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> RestoreObjectOutput:
    out: RestoreObjectOutput = {}  # type: ignore[typeddict-item]
    return out

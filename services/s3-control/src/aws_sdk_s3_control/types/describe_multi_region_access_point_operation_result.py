"""Generated from Smithy shape ``com.amazonaws.s3control#DescribeMultiRegionAccessPointOperationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.async_operation


class DescribeMultiRegionAccessPointOperationResult(TypedDict, closed=True):
    async_operation: NotRequired[
        "aws_sdk_s3_control.types.async_operation.AsyncOperation"
    ]
    """<p>A container element containing the details of the asynchronous operation.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DescribeMultiRegionAccessPointOperationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "async_operation" in value:
        import aws_sdk_s3_control.types.async_operation

        aws_sdk_s3_control.types.async_operation.serialize_xml(
            value["async_operation"], el, "AsyncOperation"
        )


def deserialize_xml(el: Element) -> DescribeMultiRegionAccessPointOperationResult:
    out: DescribeMultiRegionAccessPointOperationResult = {}  # type: ignore[typeddict-item]
    child_async_operation = el.find("AsyncOperation")
    if child_async_operation is not None:
        import aws_sdk_s3_control.types.async_operation

        out["async_operation"] = (
            aws_sdk_s3_control.types.async_operation.deserialize_xml(
                child_async_operation
            )
        )
    return out

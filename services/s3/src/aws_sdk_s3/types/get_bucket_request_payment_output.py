"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketRequestPaymentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.payer


class GetBucketRequestPaymentOutput(TypedDict):
    payer: NotRequired["aws_sdk_s3.types.payer.Payer"]
    """<p>Specifies who pays for the download and request fees.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketRequestPaymentOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "payer" in value:
        import aws_sdk_s3.types.payer

        aws_sdk_s3.types.payer.serialize_xml(value["payer"], el, "Payer")


def deserialize_xml(el: Element) -> GetBucketRequestPaymentOutput:
    out: GetBucketRequestPaymentOutput = {}  # type: ignore[typeddict-item]
    child_payer = el.find("Payer")
    if child_payer is not None:
        import aws_sdk_s3.types.payer

        out["payer"] = aws_sdk_s3.types.payer.deserialize_xml(child_payer)
    return out

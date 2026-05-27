"""Generated from Smithy shape ``com.amazonaws.s3#RequestPaymentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.payer


class RequestPaymentConfiguration(TypedDict):
    payer: "aws_sdk_s3.types.payer.Payer"
    """<p>Specifies who pays for the download and request fees.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: RequestPaymentConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.payer

    aws_sdk_s3.types.payer.serialize_xml(value["payer"], el, "Payer")


def deserialize_xml(el: Element) -> RequestPaymentConfiguration:
    out: RequestPaymentConfiguration = {}  # type: ignore[typeddict-item]
    child_payer = el.find("Payer")
    if child_payer is not None:
        import aws_sdk_s3.types.payer

        out["payer"] = aws_sdk_s3.types.payer.deserialize_xml(child_payer)
    else:
        raise DeserializationError("RequestPaymentConfiguration.payer required")
    return out

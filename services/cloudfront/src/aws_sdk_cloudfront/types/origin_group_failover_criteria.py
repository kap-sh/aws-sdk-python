"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroupFailoverCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.status_codes


class OriginGroupFailoverCriteria(TypedDict, closed=True):
    status_codes: "aws_sdk_cloudfront.types.status_codes.StatusCodes"
    """<p>The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: OriginGroupFailoverCriteria, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.status_codes

    aws_sdk_cloudfront.types.status_codes.serialize_xml(
        value["status_codes"], el, "StatusCodes"
    )


def deserialize_xml(el: Element) -> OriginGroupFailoverCriteria:
    out: OriginGroupFailoverCriteria = {}  # type: ignore[typeddict-item]
    child_status_codes = el.find("StatusCodes")
    if child_status_codes is not None:
        import aws_sdk_cloudfront.types.status_codes

        out["status_codes"] = aws_sdk_cloudfront.types.status_codes.deserialize_xml(
            child_status_codes
        )
    else:
        raise DeserializationError("OriginGroupFailoverCriteria.status_codes required")
    return out

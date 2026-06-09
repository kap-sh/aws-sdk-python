"""Generated from Smithy shape ``com.amazonaws.s3#GlacierJobParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.tier


class GlacierJobParameters(TypedDict):
    tier: "aws_sdk_s3.types.tier.Tier"
    """<p>Retrieval tier at which the restore will be processed.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GlacierJobParameters, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.tier

    aws_sdk_s3.types.tier.serialize_xml(value["tier"], el, "Tier")


def deserialize_xml(el: Element) -> GlacierJobParameters:
    out: GlacierJobParameters = {}  # type: ignore[typeddict-item]
    child_tier = el.find("Tier")
    if child_tier is not None:
        import aws_sdk_s3.types.tier

        out["tier"] = aws_sdk_s3.types.tier.deserialize_xml(child_tier)
    else:
        raise DeserializationError("GlacierJobParameters.tier required")
    return out

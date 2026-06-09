"""Generated from Smithy shape ``com.amazonaws.s3#OwnershipControls``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.ownership_controls_rules


class OwnershipControls(TypedDict):
    rules: "aws_sdk_s3.types.ownership_controls_rules.OwnershipControlsRules"
    """<p>The container element for an ownership control rule.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OwnershipControls, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.ownership_controls_rules

    aws_sdk_s3.types.ownership_controls_rules.serialize_xml_flat(
        value["rules"], el, "Rule"
    )


def deserialize_xml(el: Element) -> OwnershipControls:
    out: OwnershipControls = {}  # type: ignore[typeddict-item]
    if el.find("Rule") is not None:
        import aws_sdk_s3.types.ownership_controls_rules

        out["rules"] = aws_sdk_s3.types.ownership_controls_rules.deserialize_xml_flat(
            el, "Rule"
        )
    else:
        raise DeserializationError("OwnershipControls.rules required")
    return out

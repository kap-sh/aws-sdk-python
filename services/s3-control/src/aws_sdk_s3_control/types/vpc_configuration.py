"""Generated from Smithy shape ``com.amazonaws.s3control#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.vpc_id


class VpcConfiguration(TypedDict, closed=True):
    vpc_id: "aws_sdk_s3_control.types.vpc_id.VpcId"
    """<p>If this field is specified, this access point will only allow connections from the specified VPC ID.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: VpcConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "VpcId").text = str(value["vpc_id"])


def deserialize_xml(el: Element) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    else:
        raise DeserializationError("VpcConfiguration.vpc_id required")
    return out

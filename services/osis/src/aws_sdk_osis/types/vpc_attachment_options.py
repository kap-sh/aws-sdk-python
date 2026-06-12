"""Generated from Smithy shape ``com.amazonaws.osis#VpcAttachmentOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.boolean
    import aws_sdk_osis.types.cidr_block


class VpcAttachmentOptions(TypedDict):
    attach_to_vpc: "aws_sdk_osis.types.boolean.Boolean"
    """<p>Whether a VPC is attached to the pipeline.</p>"""
    cidr_block: NotRequired["aws_sdk_osis.types.cidr_block.CidrBlock"]
    """<p>The CIDR block to be reserved for OpenSearch Ingestion to create elastic network interfaces (ENIs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcAttachmentOptions) -> dict:
    out: dict = {}
    out["AttachToVpc"] = value["attach_to_vpc"]
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    return out


def deserialize_json(data: dict) -> VpcAttachmentOptions:
    out: VpcAttachmentOptions = {}  # type: ignore[typeddict-item]
    if "AttachToVpc" in data:
        out["attach_to_vpc"] = data["AttachToVpc"]
    else:
        raise DeserializationError("VpcAttachmentOptions.attach_to_vpc required")
    if "CidrBlock" in data:
        out["cidr_block"] = data["CidrBlock"]
    return out

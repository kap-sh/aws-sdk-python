"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionIdOwner``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DistributionIdOwner(TypedDict):
    distribution_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the distribution.</p>"""
    owner_account_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the Amazon Web Services account that owns the distribution. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionIdOwner, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "DistributionId").text = str(value["distribution_id"])
    SubElement(el, "OwnerAccountId").text = str(value["owner_account_id"])


def deserialize_xml(el: Element) -> DistributionIdOwner:
    out: DistributionIdOwner = {}  # type: ignore[typeddict-item]
    child_distribution_id = el.find("DistributionId")
    if child_distribution_id is not None:
        out["distribution_id"] = str(child_distribution_id.text or "")
    else:
        raise DeserializationError("DistributionIdOwner.distribution_id required")
    child_owner_account_id = el.find("OwnerAccountId")
    if child_owner_account_id is not None:
        out["owner_account_id"] = str(child_owner_account_id.text or "")
    else:
        raise DeserializationError("DistributionIdOwner.owner_account_id required")
    return out

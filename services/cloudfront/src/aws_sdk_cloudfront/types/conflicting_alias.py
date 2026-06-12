"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConflictingAlias``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class ConflictingAlias(TypedDict):
    alias: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>An alias (also called a CNAME).</p>"""
    distribution_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The (partially hidden) ID of the CloudFront standard distribution associated with the alias.</p>"""
    account_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The (partially hidden) ID of the Amazon Web Services account that owns the standard distribution that's associated with the alias.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ConflictingAlias, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "alias" in value:
        SubElement(el, "Alias").text = str(value["alias"])
    if "distribution_id" in value:
        SubElement(el, "DistributionId").text = str(value["distribution_id"])
    if "account_id" in value:
        SubElement(el, "AccountId").text = str(value["account_id"])


def deserialize_xml(el: Element) -> ConflictingAlias:
    out: ConflictingAlias = {}  # type: ignore[typeddict-item]
    child_alias = el.find("Alias")
    if child_alias is not None:
        out["alias"] = str(child_alias.text or "")
    child_distribution_id = el.find("DistributionId")
    if child_distribution_id is not None:
        out["distribution_id"] = str(child_distribution_id.text or "")
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    return out

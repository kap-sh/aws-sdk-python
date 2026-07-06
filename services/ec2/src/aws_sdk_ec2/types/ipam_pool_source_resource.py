"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolSourceResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_source_resource_type
    import aws_sdk_ec2.types.string


class IpamPoolSourceResource(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source resource ID.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_source_resource_type.IpamPoolSourceResourceType"
    ]
    """<p>The source resource type.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source resource Region.</p>"""
    resource_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source resource owner.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolSourceResource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.ipam_pool_source_resource_type

        aws_sdk_ec2.types.ipam_pool_source_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_region" in value:
        pairs.append((f"{prefix}.ResourceRegion", str(value["resource_region"])))
    if "resource_owner" in value:
        pairs.append((f"{prefix}.ResourceOwner", str(value["resource_owner"])))


def deserialize_ec2_query(el: Element) -> IpamPoolSourceResource:
    out: IpamPoolSourceResource = {}  # type: ignore[typeddict-item]
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.ipam_pool_source_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.ipam_pool_source_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_region = el.find("ResourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    return out

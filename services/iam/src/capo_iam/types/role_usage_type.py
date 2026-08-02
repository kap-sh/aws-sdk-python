"""Generated from Smithy shape ``com.amazonaws.iam#RoleUsageType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_list_type
    import capo_iam.types.region_name_type


class RoleUsageType(TypedDict, closed=True):
    region: NotRequired["capo_iam.types.region_name_type.RegionNameType"]
    """<p>The name of the Region where the service-linked role is being used.</p>"""
    resources: NotRequired["capo_iam.types.arn_list_type.ArnListType"]
    """<p>The name of the resource that is using the service-linked role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleUsageType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "resources" in value:
        import capo_iam.types.arn_list_type

        capo_iam.types.arn_list_type.serialize_query(
            value["resources"], pairs, f"{key_prefix}Resources"
        )


def deserialize_query(el: Element) -> RoleUsageType:
    out: RoleUsageType = {}  # type: ignore[typeddict-item]
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_resources = el.find("Resources")
    if child_resources is not None:
        import capo_iam.types.arn_list_type

        out["resources"] = capo_iam.types.arn_list_type.deserialize_query(
            child_resources
        )
    return out

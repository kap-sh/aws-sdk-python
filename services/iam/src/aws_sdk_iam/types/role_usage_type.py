"""Generated from Smithy shape ``com.amazonaws.iam#RoleUsageType``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_list_type
    import aws_sdk_iam.types.region_name_type


class RoleUsageType(TypedDict):
    region: NotRequired["aws_sdk_iam.types.region_name_type.RegionNameType"]
    """<p>The name of the Region where the service-linked role is being used.</p>"""
    resources: NotRequired["aws_sdk_iam.types.arn_list_type.ArnListType"]
    """<p>The name of the resource that is using the service-linked role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleUsageType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "region" in value:
        pairs.append((f"{prefix}.Region", str(value["region"])))
    if "resources" in value:
        import aws_sdk_iam.types.arn_list_type

        aws_sdk_iam.types.arn_list_type.serialize_query(
            value["resources"], pairs, f"{prefix}.Resources"
        )


def deserialize_query(el: Element) -> RoleUsageType:
    out: RoleUsageType = {}  # type: ignore[typeddict-item]
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_resources = el.find("Resources")
    if child_resources is not None:
        import aws_sdk_iam.types.arn_list_type

        out["resources"] = aws_sdk_iam.types.arn_list_type.deserialize_query(
            child_resources
        )
    return out

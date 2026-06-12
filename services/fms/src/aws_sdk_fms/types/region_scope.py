"""Generated from Smithy shape ``com.amazonaws.fms#RegionScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_region_list
    import aws_sdk_fms.types.boolean


class RegionScope(TypedDict):
    regions: NotRequired["aws_sdk_fms.types.aws_region_list.AWSRegionList"]
    """<p>The Amazon Web Services Regions that the specified Firewall Manager administrator can perform actions in.</p>"""
    all_regions_enabled: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Allows the specified Firewall Manager administrator to manage all Amazon Web Services Regions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionScope) -> dict:
    out: dict = {}
    if "regions" in value:
        import aws_sdk_fms.types.aws_region_list

        out["Regions"] = aws_sdk_fms.types.aws_region_list.serialize_aws_json_1_1(
            value["regions"]
        )
    out["AllRegionsEnabled"] = value.get("all_regions_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionScope:
    out: RegionScope = {}  # type: ignore[typeddict-item]
    if "Regions" in data:
        import aws_sdk_fms.types.aws_region_list

        out["regions"] = aws_sdk_fms.types.aws_region_list.deserialize_aws_json_1_1(
            data["Regions"]
        )
    if "AllRegionsEnabled" in data:
        out["all_regions_enabled"] = data["AllRegionsEnabled"]
    else:
        out["all_regions_enabled"] = False
    return out

"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RegionMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.date
    import aws_sdk_sso_admin.types.is_primary_region
    import aws_sdk_sso_admin.types.region_name
    import aws_sdk_sso_admin.types.region_status


class RegionMetadata(TypedDict):
    region_name: NotRequired["aws_sdk_sso_admin.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region name.</p>"""
    status: NotRequired["aws_sdk_sso_admin.types.region_status.RegionStatus"]
    """<p>The current status of the Region. Valid values are ACTIVE (Region is operational), ADDING (Region extension workflow is in progress), or REMOVING (Region removal workflow is in progress).</p>"""
    added_date: NotRequired["aws_sdk_sso_admin.types.date.Date"]
    """<p>The timestamp when the Region was added to the IAM Identity Center instance. For the primary Region, this is the instance creation time.</p>"""
    is_primary_region: "aws_sdk_sso_admin.types.is_primary_region.IsPrimaryRegion"
    """<p>Indicates whether this is the primary Region where the IAM Identity Center instance was originally enabled. The primary Region cannot be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionMetadata) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "status" in value:
        import aws_sdk_sso_admin.types.region_status

        out["Status"] = aws_sdk_sso_admin.types.region_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "added_date" in value:
        import aws_sdk_sso_admin.types.date

        out["AddedDate"] = aws_sdk_sso_admin.types.date.serialize_aws_json_1_1(
            value["added_date"]
        )
    out["IsPrimaryRegion"] = value.get("is_primary_region", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionMetadata:
    out: RegionMetadata = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "Status" in data:
        import aws_sdk_sso_admin.types.region_status

        out["status"] = aws_sdk_sso_admin.types.region_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "AddedDate" in data:
        import aws_sdk_sso_admin.types.date

        out["added_date"] = aws_sdk_sso_admin.types.date.deserialize_aws_json_1_1(
            data["AddedDate"]
        )
    if "IsPrimaryRegion" in data:
        out["is_primary_region"] = data["IsPrimaryRegion"]
    else:
        out["is_primary_region"] = False
    return out

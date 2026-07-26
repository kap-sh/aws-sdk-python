"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListRegionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.region_metadata_list
    import capo_sso_admin.types.token


class ListRegionsResponse(TypedDict, closed=True):
    regions: NotRequired["capo_sso_admin.types.region_metadata_list.RegionMetadataList"]
    """<p>The list of Regions enabled in the IAM Identity Center instance, including Regions with ACTIVE, ADDING, or REMOVING status.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token to be used in subsequent calls. If the value is null, then there are no more entries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRegionsResponse) -> dict:
    out: dict = {}
    if "regions" in value:
        import capo_sso_admin.types.region_metadata_list

        out["Regions"] = (
            capo_sso_admin.types.region_metadata_list.serialize_aws_json_1_1(
                value["regions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRegionsResponse:
    out: ListRegionsResponse = {}  # type: ignore[typeddict-item]
    if "Regions" in data:
        import capo_sso_admin.types.region_metadata_list

        out["regions"] = (
            capo_sso_admin.types.region_metadata_list.deserialize_aws_json_1_1(
                data["Regions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

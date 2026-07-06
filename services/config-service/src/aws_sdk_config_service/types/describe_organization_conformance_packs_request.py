"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeOrganizationConformancePacksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.cosmos_page_limit
    import aws_sdk_config_service.types.organization_conformance_pack_names
    import aws_sdk_config_service.types.string


class DescribeOrganizationConformancePacksRequest(TypedDict, closed=True):
    organization_conformance_pack_names: NotRequired[
        "aws_sdk_config_service.types.organization_conformance_pack_names.OrganizationConformancePackNames"
    ]
    """<p>The name that you assign to an organization conformance pack.</p>"""
    limit: "aws_sdk_config_service.types.cosmos_page_limit.CosmosPageLimit"
    """<p>The maximum number of organization config packs returned on each page. If you do no specify a number, Config uses the default. The default is 100.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrganizationConformancePacksRequest) -> dict:
    out: dict = {}
    if "organization_conformance_pack_names" in value:
        import aws_sdk_config_service.types.organization_conformance_pack_names

        out["OrganizationConformancePackNames"] = (
            aws_sdk_config_service.types.organization_conformance_pack_names.serialize_aws_json_1_1(
                value["organization_conformance_pack_names"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOrganizationConformancePacksRequest:
    out: DescribeOrganizationConformancePacksRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationConformancePackNames" in data:
        import aws_sdk_config_service.types.organization_conformance_pack_names

        out["organization_conformance_pack_names"] = (
            aws_sdk_config_service.types.organization_conformance_pack_names.deserialize_aws_json_1_1(
                data["OrganizationConformancePackNames"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

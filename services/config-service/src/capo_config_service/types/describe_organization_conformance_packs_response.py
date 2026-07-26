"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeOrganizationConformancePacksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.organization_conformance_packs
    import capo_config_service.types.string


class DescribeOrganizationConformancePacksResponse(TypedDict, closed=True):
    organization_conformance_packs: NotRequired[
        "capo_config_service.types.organization_conformance_packs.OrganizationConformancePacks"
    ]
    """<p>Returns a list of OrganizationConformancePacks objects.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrganizationConformancePacksResponse) -> dict:
    out: dict = {}
    if "organization_conformance_packs" in value:
        import capo_config_service.types.organization_conformance_packs

        out["OrganizationConformancePacks"] = (
            capo_config_service.types.organization_conformance_packs.serialize_aws_json_1_1(
                value["organization_conformance_packs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeOrganizationConformancePacksResponse:
    out: DescribeOrganizationConformancePacksResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationConformancePacks" in data:
        import capo_config_service.types.organization_conformance_packs

        out["organization_conformance_packs"] = (
            capo_config_service.types.organization_conformance_packs.deserialize_aws_json_1_1(
                data["OrganizationConformancePacks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

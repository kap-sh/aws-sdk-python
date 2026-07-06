"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeOrganizationConformancePackStatusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_conformance_pack_statuses
    import aws_sdk_config_service.types.string


class DescribeOrganizationConformancePackStatusesResponse(TypedDict, closed=True):
    organization_conformance_pack_statuses: NotRequired[
        "aws_sdk_config_service.types.organization_conformance_pack_statuses.OrganizationConformancePackStatuses"
    ]
    """<p>A list of <code>OrganizationConformancePackStatus</code> objects. </p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeOrganizationConformancePackStatusesResponse,
) -> dict:
    out: dict = {}
    if "organization_conformance_pack_statuses" in value:
        import aws_sdk_config_service.types.organization_conformance_pack_statuses

        out["OrganizationConformancePackStatuses"] = (
            aws_sdk_config_service.types.organization_conformance_pack_statuses.serialize_aws_json_1_1(
                value["organization_conformance_pack_statuses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeOrganizationConformancePackStatusesResponse:
    out: DescribeOrganizationConformancePackStatusesResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationConformancePackStatuses" in data:
        import aws_sdk_config_service.types.organization_conformance_pack_statuses

        out["organization_conformance_pack_statuses"] = (
            aws_sdk_config_service.types.organization_conformance_pack_statuses.deserialize_aws_json_1_1(
                data["OrganizationConformancePackStatuses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#GetOrganizationStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.organization_details


class GetOrganizationStatisticsResponse(TypedDict, closed=True):
    organization_details: NotRequired[
        "capo_guardduty.types.organization_details.OrganizationDetails"
    ]
    """<p>Information about the statistics report for your organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOrganizationStatisticsResponse) -> dict:
    out: dict = {}
    if "organization_details" in value:
        import capo_guardduty.types.organization_details

        out["organizationDetails"] = (
            capo_guardduty.types.organization_details.serialize_json(
                value["organization_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetOrganizationStatisticsResponse:
    out: GetOrganizationStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "organizationDetails" in data:
        import capo_guardduty.types.organization_details

        out["organization_details"] = (
            capo_guardduty.types.organization_details.deserialize_json(
                data["organizationDetails"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.organization_statistics
    import aws_sdk_guardduty.types.timestamp


class OrganizationDetails(TypedDict, closed=True):
    updated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the organization statistics was last updated. This is in UTC format.</p>"""
    organization_statistics: NotRequired[
        "aws_sdk_guardduty.types.organization_statistics.OrganizationStatistics"
    ]
    """<p>Information about the GuardDuty coverage statistics for members in your Amazon Web Services organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationDetails) -> dict:
    out: dict = {}
    if "updated_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["updatedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "organization_statistics" in value:
        import aws_sdk_guardduty.types.organization_statistics

        out["organizationStatistics"] = (
            aws_sdk_guardduty.types.organization_statistics.serialize_json(
                value["organization_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationDetails:
    out: OrganizationDetails = {}  # type: ignore[typeddict-item]
    if "updatedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["updated_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "organizationStatistics" in data:
        import aws_sdk_guardduty.types.organization_statistics

        out["organization_statistics"] = (
            aws_sdk_guardduty.types.organization_statistics.deserialize_json(
                data["organizationStatistics"]
            )
        )
    return out

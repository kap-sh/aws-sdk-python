"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationScanEc2InstanceWithFindings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.organization_ebs_volumes


class OrganizationScanEc2InstanceWithFindings(TypedDict, closed=True):
    ebs_volumes: NotRequired[
        "aws_sdk_guardduty.types.organization_ebs_volumes.OrganizationEbsVolumes"
    ]
    """<p>Whether scanning EBS volumes should be auto-enabled for new members joining the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationScanEc2InstanceWithFindings) -> dict:
    out: dict = {}
    if "ebs_volumes" in value:
        import aws_sdk_guardduty.types.organization_ebs_volumes

        out["ebsVolumes"] = (
            aws_sdk_guardduty.types.organization_ebs_volumes.serialize_json(
                value["ebs_volumes"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationScanEc2InstanceWithFindings:
    out: OrganizationScanEc2InstanceWithFindings = {}  # type: ignore[typeddict-item]
    if "ebsVolumes" in data:
        import aws_sdk_guardduty.types.organization_ebs_volumes

        out["ebs_volumes"] = (
            aws_sdk_guardduty.types.organization_ebs_volumes.deserialize_json(
                data["ebsVolumes"]
            )
        )
    return out

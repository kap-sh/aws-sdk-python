"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_details
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDetails(TypedDict, closed=True):
    launch_template_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A name for the launch template. </p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> An ID for the launch template. </p>"""
    launch_template_data: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_details.AwsEc2LaunchTemplateDataDetails"
    ]
    """<p> The information to include in the launch template. </p>"""
    default_version_number: NotRequired["capo_securityhub.types.long.Long"]
    """<p> The default version of the launch template. </p>"""
    latest_version_number: NotRequired["capo_securityhub.types.long.Long"]
    """<p> The latest version of the launch template. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDetails) -> dict:
    out: dict = {}
    if "launch_template_name" in value:
        out["LaunchTemplateName"] = value["launch_template_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "launch_template_data" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_details

        out["LaunchTemplateData"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_details.serialize_json(
                value["launch_template_data"]
            )
        )
    if "default_version_number" in value:
        out["DefaultVersionNumber"] = value["default_version_number"]
    if "latest_version_number" in value:
        out["LatestVersionNumber"] = value["latest_version_number"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDetails:
    out: AwsEc2LaunchTemplateDetails = {}  # type: ignore[typeddict-item]
    if "LaunchTemplateName" in data:
        out["launch_template_name"] = data["LaunchTemplateName"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "LaunchTemplateData" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_details

        out["launch_template_data"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_details.deserialize_json(
                data["LaunchTemplateData"]
            )
        )
    if "DefaultVersionNumber" in data:
        out["default_version_number"] = data["DefaultVersionNumber"]
    if "LatestVersionNumber" in data:
        out["latest_version_number"] = data["LatestVersionNumber"]
    return out

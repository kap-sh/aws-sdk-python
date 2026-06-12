"""Generated from Smithy shape ``com.amazonaws.drs#DescribeLaunchConfigurationTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_configuration_template_i_ds
    import aws_sdk_drs.types.max_results_type
    import aws_sdk_drs.types.pagination_token

class DescribeLaunchConfigurationTemplatesRequest(TypedDict):
    launch_configuration_template_i_ds: NotRequired["aws_sdk_drs.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"]
    """<p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>"""
    max_results: NotRequired["aws_sdk_drs.types.max_results_type.MaxResultsType"]
    """<p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Launch Configuration Template to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeLaunchConfigurationTemplatesRequest) -> dict:
    out: dict = {}
    if "launch_configuration_template_i_ds" in value:
        import aws_sdk_drs.types.launch_configuration_template_i_ds
        out["launchConfigurationTemplateIDs"] = aws_sdk_drs.types.launch_configuration_template_i_ds.serialize_json(value["launch_configuration_template_i_ds"])
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeLaunchConfigurationTemplatesRequest:
    out: DescribeLaunchConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "launchConfigurationTemplateIDs" in data:
        import aws_sdk_drs.types.launch_configuration_template_i_ds
        out["launch_configuration_template_i_ds"] = aws_sdk_drs.types.launch_configuration_template_i_ds.deserialize_json(data["launchConfigurationTemplateIDs"])
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
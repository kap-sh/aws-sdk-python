"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionInputs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_parameter_key
    import aws_sdk_ssm.types.automation_parameter_map
    import aws_sdk_ssm.types.target_locations
    import aws_sdk_ssm.types.target_locations_url
    import aws_sdk_ssm.types.target_maps
    import aws_sdk_ssm.types.targets


class AutomationExecutionInputs(TypedDict, closed=True):
    parameters: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>Information about parameters that can be specified for the preview operation. </p>"""
    target_parameter_name: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.</p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>Information about the resources that would be included in the actual runbook execution, if it were to be run. Both Targets and TargetMaps can't be specified together.</p>"""
    target_maps: NotRequired["aws_sdk_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""
    target_locations: NotRequired["aws_sdk_ssm.types.target_locations.TargetLocations"]
    """<p>Information about the Amazon Web Services Regions and Amazon Web Services accounts targeted by the Automation execution preview operation.</p>"""
    target_locations_url: NotRequired[
        "aws_sdk_ssm.types.target_locations_url.TargetLocationsURL"
    ]
    """<p>A publicly accessible URL for a file that contains the <code>TargetLocations</code> body. Currently, only files in presigned Amazon S3 buckets are supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionInputs) -> dict:
    out: dict = {}
    if "parameters" in value:
        import aws_sdk_ssm.types.automation_parameter_map

        out["Parameters"] = (
            aws_sdk_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "target_parameter_name" in value:
        out["TargetParameterName"] = value["target_parameter_name"]
    if "targets" in value:
        import aws_sdk_ssm.types.targets

        out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "target_maps" in value:
        import aws_sdk_ssm.types.target_maps

        out["TargetMaps"] = aws_sdk_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "target_locations" in value:
        import aws_sdk_ssm.types.target_locations

        out["TargetLocations"] = (
            aws_sdk_ssm.types.target_locations.serialize_aws_json_1_1(
                value["target_locations"]
            )
        )
    if "target_locations_url" in value:
        out["TargetLocationsURL"] = value["target_locations_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecutionInputs:
    out: AutomationExecutionInputs = {}  # type: ignore[typeddict-item]
    if "Parameters" in data:
        import aws_sdk_ssm.types.automation_parameter_map

        out["parameters"] = (
            aws_sdk_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "TargetParameterName" in data:
        out["target_parameter_name"] = data["TargetParameterName"]
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "TargetMaps" in data:
        import aws_sdk_ssm.types.target_maps

        out["target_maps"] = aws_sdk_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if "TargetLocations" in data:
        import aws_sdk_ssm.types.target_locations

        out["target_locations"] = (
            aws_sdk_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    if "TargetLocationsURL" in data:
        out["target_locations_url"] = data["TargetLocationsURL"]
    return out

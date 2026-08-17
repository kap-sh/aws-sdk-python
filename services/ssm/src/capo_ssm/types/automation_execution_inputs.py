"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionInputs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_parameter_key
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.target_locations
    import capo_ssm.types.target_locations_url
    import capo_ssm.types.target_maps
    import capo_ssm.types.targets


class AutomationExecutionInputs(TypedDict, closed=True):
    parameters: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>Information about parameters that can be specified for the preview operation. </p>"""
    target_parameter_name: NotRequired[
        "capo_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>Information about the resources that would be included in the actual runbook execution, if it were to be run. Both Targets and TargetMaps can't be specified together.</p>"""
    target_maps: NotRequired["capo_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""
    target_locations: NotRequired["capo_ssm.types.target_locations.TargetLocations"]
    """<p>Information about the Amazon Web Services Regions and Amazon Web Services accounts targeted by the Automation execution preview operation.</p>"""
    target_locations_url: NotRequired[
        "capo_ssm.types.target_locations_url.TargetLocationsURL"
    ]
    """<p>A publicly accessible URL for a file that contains the <code>TargetLocations</code> body. Currently, only files in presigned Amazon S3 buckets are supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionInputs) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_ssm.types.automation_parameter_map

        out["Parameters"] = (
            capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "target_parameter_name" in value:
        out["TargetParameterName"] = value["target_parameter_name"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "target_maps" in value:
        import capo_ssm.types.target_maps

        out["TargetMaps"] = capo_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "target_locations" in value:
        import capo_ssm.types.target_locations

        out["TargetLocations"] = capo_ssm.types.target_locations.serialize_aws_json_1_1(
            value["target_locations"]
        )
    if "target_locations_url" in value:
        out["TargetLocationsURL"] = value["target_locations_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecutionInputs:
    out: AutomationExecutionInputs = {}  # type: ignore[typeddict-item]
    if data.get("Parameters") is not None:
        import capo_ssm.types.automation_parameter_map

        out["parameters"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("TargetParameterName") is not None:
        out["target_parameter_name"] = data["TargetParameterName"]
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("TargetMaps") is not None:
        import capo_ssm.types.target_maps

        out["target_maps"] = capo_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if data.get("TargetLocations") is not None:
        import capo_ssm.types.target_locations

        out["target_locations"] = (
            capo_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    if data.get("TargetLocationsURL") is not None:
        out["target_locations_url"] = data["TargetLocationsURL"]
    return out

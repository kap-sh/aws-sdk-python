"""Generated from Smithy shape ``com.amazonaws.ssm#Runbook``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_parameter_key
    import aws_sdk_ssm.types.automation_parameter_map
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.max_concurrency
    import aws_sdk_ssm.types.max_errors
    import aws_sdk_ssm.types.target_locations
    import aws_sdk_ssm.types.target_maps
    import aws_sdk_ssm.types.targets


class Runbook(TypedDict):
    document_name: "aws_sdk_ssm.types.document_arn.DocumentARN"
    """<p>The name of the Automation runbook used in a runbook workflow.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the Automation runbook used in a runbook workflow.</p>"""
    parameters: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The key-value map of execution parameters, which were supplied when calling <code>StartChangeRequestExecution</code>.</p>"""
    target_parameter_name: NotRequired[
        "aws_sdk_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The name of the parameter used as the target resource for the rate-controlled runbook workflow. Required if you specify <code>Targets</code>. </p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>A key-value mapping to target resources that the runbook operation performs tasks on. Required if you specify <code>TargetParameterName</code>.</p>"""
    target_maps: NotRequired["aws_sdk_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of runbook parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""
    max_concurrency: NotRequired["aws_sdk_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The <code>MaxConcurrency</code> value specified by the user when the operation started, indicating the maximum number of resources that the runbook operation can run on at the same time.</p>"""
    max_errors: NotRequired["aws_sdk_ssm.types.max_errors.MaxErrors"]
    """<p>The <code>MaxErrors</code> value specified by the user when the execution started, indicating the maximum number of errors that can occur during the operation before the updates are stopped or rolled back.</p>"""
    target_locations: NotRequired["aws_sdk_ssm.types.target_locations.TargetLocations"]
    """<p>Information about the Amazon Web Services Regions and Amazon Web Services accounts targeted by the current Runbook operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Runbook) -> dict:
    out: dict = {}
    out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
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
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "target_locations" in value:
        import aws_sdk_ssm.types.target_locations

        out["TargetLocations"] = (
            aws_sdk_ssm.types.target_locations.serialize_aws_json_1_1(
                value["target_locations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Runbook:
    out: Runbook = {}  # type: ignore[typeddict-item]
    if "DocumentName" in data:
        out["document_name"] = data["DocumentName"]
    else:
        raise DeserializationError("Runbook.document_name required")
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
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
    if "MaxConcurrency" in data:
        out["max_concurrency"] = data["MaxConcurrency"]
    if "MaxErrors" in data:
        out["max_errors"] = data["MaxErrors"]
    if "TargetLocations" in data:
        import aws_sdk_ssm.types.target_locations

        out["target_locations"] = (
            aws_sdk_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#CustomActionLambdaConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.lambda_list
    import aws_sdk_arc_region_switch.types.lambda_ungraceful
    import aws_sdk_arc_region_switch.types.region_to_run_in


class CustomActionLambdaConfiguration(TypedDict):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    lambdas: "aws_sdk_arc_region_switch.types.lambda_list.LambdaList"
    """<p>The Amazon Web Services Lambda functions for the execution block.</p>"""
    retry_interval_minutes: "float"
    """<p>The retry interval specified.</p>"""
    region_to_run: "aws_sdk_arc_region_switch.types.region_to_run_in.RegionToRunIn"
    """<p>The Amazon Web Services Region for the function to run in. For recovery workflows use <code>activatingRegion</code> or <code>deactivatingRegion</code>. For post-recovery workflows, use <code>activeRegion</code> (the Region with customer traffic) or <code>inactiveRegion</code> (the Region with no customer traffic).</p>"""
    ungraceful: NotRequired[
        "aws_sdk_arc_region_switch.types.lambda_ungraceful.LambdaUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomActionLambdaConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import aws_sdk_arc_region_switch.types.lambda_list

    out["lambdas"] = aws_sdk_arc_region_switch.types.lambda_list.serialize_aws_json_1_0(
        value["lambdas"]
    )
    out["retryIntervalMinutes"] = value["retry_interval_minutes"]
    import aws_sdk_arc_region_switch.types.region_to_run_in

    out["regionToRun"] = (
        aws_sdk_arc_region_switch.types.region_to_run_in.serialize_aws_json_1_0(
            value["region_to_run"]
        )
    )
    if "ungraceful" in value:
        import aws_sdk_arc_region_switch.types.lambda_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.lambda_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomActionLambdaConfiguration:
    out: CustomActionLambdaConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "lambdas" in data:
        import aws_sdk_arc_region_switch.types.lambda_list

        out["lambdas"] = (
            aws_sdk_arc_region_switch.types.lambda_list.deserialize_aws_json_1_0(
                data["lambdas"]
            )
        )
    else:
        raise DeserializationError("CustomActionLambdaConfiguration.lambdas required")
    if "retryIntervalMinutes" in data:
        out["retry_interval_minutes"] = data["retryIntervalMinutes"]
    else:
        raise DeserializationError(
            "CustomActionLambdaConfiguration.retry_interval_minutes required"
        )
    if "regionToRun" in data:
        import aws_sdk_arc_region_switch.types.region_to_run_in

        out["region_to_run"] = (
            aws_sdk_arc_region_switch.types.region_to_run_in.deserialize_aws_json_1_0(
                data["regionToRun"]
            )
        )
    else:
        raise DeserializationError(
            "CustomActionLambdaConfiguration.region_to_run required"
        )
    if "ungraceful" in data:
        import aws_sdk_arc_region_switch.types.lambda_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.lambda_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    return out

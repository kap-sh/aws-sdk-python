"""Generated from Smithy shape ``com.amazonaws.arczonalshift#CreatePracticeRunConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.practice_run_configuration
    import aws_sdk_arc_zonal_shift.types.resource_arn
    import aws_sdk_arc_zonal_shift.types.resource_name
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status


class CreatePracticeRunConfigurationResponse(TypedDict):
    arn: "aws_sdk_arc_zonal_shift.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you configured the practice run for.</p>"""
    name: "aws_sdk_arc_zonal_shift.types.resource_name.ResourceName"
    """<p>The name of the resource that you configured the practice run for. </p>"""
    zonal_autoshift_status: (
        "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The status for zonal autoshift for a resource. When you specify <code>ENABLED</code> for the autoshift status, Amazon Web Services shifts traffic away from shifts away application resource traffic from an Availability Zone, on your behalf, when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers.</p> <p>When you enable zonal autoshift, you must also configure practice runs for the resource.</p>"""
    practice_run_configuration: "aws_sdk_arc_zonal_shift.types.practice_run_configuration.PracticeRunConfiguration"
    """<p>A practice run configuration for a resource. Configurations include the outcome alarm that you specify for practice runs, and, optionally, a blocking alarm and blocking dates and windows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePracticeRunConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

    out["zonalAutoshiftStatus"] = (
        aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
            value["zonal_autoshift_status"]
        )
    )
    import aws_sdk_arc_zonal_shift.types.practice_run_configuration

    out["practiceRunConfiguration"] = (
        aws_sdk_arc_zonal_shift.types.practice_run_configuration.serialize_json(
            value["practice_run_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePracticeRunConfigurationResponse:
    out: CreatePracticeRunConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "CreatePracticeRunConfigurationResponse.arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreatePracticeRunConfigurationResponse.name required"
        )
    if "zonalAutoshiftStatus" in data:
        import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

        out["zonal_autoshift_status"] = (
            aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.deserialize_json(
                data["zonalAutoshiftStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePracticeRunConfigurationResponse.zonal_autoshift_status required"
        )
    if "practiceRunConfiguration" in data:
        import aws_sdk_arc_zonal_shift.types.practice_run_configuration

        out["practice_run_configuration"] = (
            aws_sdk_arc_zonal_shift.types.practice_run_configuration.deserialize_json(
                data["practiceRunConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePracticeRunConfigurationResponse.practice_run_configuration required"
        )
    return out

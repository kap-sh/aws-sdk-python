"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdatePracticeRunConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.practice_run_configuration
    import aws_sdk_arc_zonal_shift.types.resource_arn
    import aws_sdk_arc_zonal_shift.types.resource_name
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status


class UpdatePracticeRunConfigurationResponse(TypedDict):
    arn: "aws_sdk_arc_zonal_shift.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you updated the practice run for.</p>"""
    name: "aws_sdk_arc_zonal_shift.types.resource_name.ResourceName"
    """<p>The name of the resource that you updated the practice run for. </p>"""
    zonal_autoshift_status: (
        "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The zonal autoshift status for the resource that you updated the practice run for.</p>"""
    practice_run_configuration: "aws_sdk_arc_zonal_shift.types.practice_run_configuration.PracticeRunConfiguration"
    """<p>The practice run configuration that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePracticeRunConfigurationResponse) -> dict:
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


def deserialize_json(data: dict) -> UpdatePracticeRunConfigurationResponse:
    out: UpdatePracticeRunConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "UpdatePracticeRunConfigurationResponse.arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "UpdatePracticeRunConfigurationResponse.name required"
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
            "UpdatePracticeRunConfigurationResponse.zonal_autoshift_status required"
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
            "UpdatePracticeRunConfigurationResponse.practice_run_configuration required"
        )
    return out

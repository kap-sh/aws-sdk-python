"""Generated from Smithy shape ``com.amazonaws.arczonalshift#DeletePracticeRunConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.resource_arn
    import aws_sdk_arc_zonal_shift.types.resource_name
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status


class DeletePracticeRunConfigurationResponse(TypedDict, closed=True):
    arn: "aws_sdk_arc_zonal_shift.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you deleted the practice run for.</p>"""
    name: "aws_sdk_arc_zonal_shift.types.resource_name.ResourceName"
    """<p>The name of the resource that you deleted the practice run for. </p>"""
    zonal_autoshift_status: (
        "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The status of zonal autoshift for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePracticeRunConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

    out["zonalAutoshiftStatus"] = (
        aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
            value["zonal_autoshift_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeletePracticeRunConfigurationResponse:
    out: DeletePracticeRunConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "DeletePracticeRunConfigurationResponse.arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "DeletePracticeRunConfigurationResponse.name required"
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
            "DeletePracticeRunConfigurationResponse.zonal_autoshift_status required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateZonalAutoshiftConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.resource_identifier
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status


class UpdateZonalAutoshiftConfigurationResponse(TypedDict):
    resource_identifier: (
        "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that you updated the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""
    zonal_autoshift_status: (
        "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The updated zonal autoshift status for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateZonalAutoshiftConfigurationResponse) -> dict:
    out: dict = {}
    out["resourceIdentifier"] = value["resource_identifier"]
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

    out["zonalAutoshiftStatus"] = (
        aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
            value["zonal_autoshift_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateZonalAutoshiftConfigurationResponse:
    out: UpdateZonalAutoshiftConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "resourceIdentifier" in data:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError(
            "UpdateZonalAutoshiftConfigurationResponse.resource_identifier required"
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
            "UpdateZonalAutoshiftConfigurationResponse.zonal_autoshift_status required"
        )
    return out

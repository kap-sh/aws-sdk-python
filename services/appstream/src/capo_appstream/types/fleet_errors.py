"""Generated from Smithy shape ``com.amazonaws.appstream#FleetErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.fleet_error

FleetErrors: TypeAlias = list["capo_appstream.types.fleet_error.FleetError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetErrors) -> list:
    import capo_appstream.types.fleet_error

    out: list = []
    for item in value:
        out.append(capo_appstream.types.fleet_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetErrors:
    import capo_appstream.types.fleet_error

    out: FleetErrors = []
    for item in data:
        out.append(capo_appstream.types.fleet_error.deserialize_aws_json_1_1(item))
    return out

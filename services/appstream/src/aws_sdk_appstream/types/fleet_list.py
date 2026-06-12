"""Generated from Smithy shape ``com.amazonaws.appstream#FleetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.fleet

FleetList: TypeAlias = list["aws_sdk_appstream.types.fleet.Fleet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetList) -> list:
    import aws_sdk_appstream.types.fleet

    out: list = []
    for item in value:
        out.append(aws_sdk_appstream.types.fleet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FleetList:
    import aws_sdk_appstream.types.fleet

    out: FleetList = []
    for item in data:
        out.append(aws_sdk_appstream.types.fleet.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleAssociationBehavior``."""

from typing import Literal, TypeAlias, cast

VehicleAssociationBehavior: TypeAlias = Literal[
    "CreateIotThing",
    "ValidateIotThingExists",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleAssociationBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VehicleAssociationBehavior:
    return cast(VehicleAssociationBehavior, data)

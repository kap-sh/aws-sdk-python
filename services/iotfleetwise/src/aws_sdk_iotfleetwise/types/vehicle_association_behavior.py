"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleAssociationBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

VehicleAssociationBehavior: TypeAlias = Literal[
    "CreateIotThing",
    "ValidateIotThingExists",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreateIotThing",
        "ValidateIotThingExists",
    )
)


def serialize_aws_json_1_0(value: VehicleAssociationBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VehicleAssociationBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VehicleAssociationBehavior value: {data!r}"
        )
    return cast(VehicleAssociationBehavior, data)

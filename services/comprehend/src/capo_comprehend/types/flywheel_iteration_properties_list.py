"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelIterationPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_iteration_properties

FlywheelIterationPropertiesList: TypeAlias = list[
    "capo_comprehend.types.flywheel_iteration_properties.FlywheelIterationProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelIterationPropertiesList) -> list:
    import capo_comprehend.types.flywheel_iteration_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.flywheel_iteration_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FlywheelIterationPropertiesList:
    import capo_comprehend.types.flywheel_iteration_properties

    out: FlywheelIterationPropertiesList = []
    for item in data:
        out.append(
            capo_comprehend.types.flywheel_iteration_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out

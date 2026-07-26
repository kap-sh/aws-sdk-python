"""Generated from Smithy shape ``com.amazonaws.athena#GetCapacityAssignmentConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.capacity_assignment_configuration


class GetCapacityAssignmentConfigurationOutput(TypedDict, closed=True):
    capacity_assignment_configuration: "capo_athena.types.capacity_assignment_configuration.CapacityAssignmentConfiguration"
    """<p>The requested capacity assignment configuration for the specified capacity reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCapacityAssignmentConfigurationOutput) -> dict:
    out: dict = {}
    import capo_athena.types.capacity_assignment_configuration

    out["CapacityAssignmentConfiguration"] = (
        capo_athena.types.capacity_assignment_configuration.serialize_aws_json_1_1(
            value["capacity_assignment_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCapacityAssignmentConfigurationOutput:
    out: GetCapacityAssignmentConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "CapacityAssignmentConfiguration" in data:
        import capo_athena.types.capacity_assignment_configuration

        out["capacity_assignment_configuration"] = (
            capo_athena.types.capacity_assignment_configuration.deserialize_aws_json_1_1(
                data["CapacityAssignmentConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetCapacityAssignmentConfigurationOutput.capacity_assignment_configuration required"
        )
    return out

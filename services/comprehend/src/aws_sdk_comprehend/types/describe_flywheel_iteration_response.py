"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeFlywheelIterationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.flywheel_iteration_properties


class DescribeFlywheelIterationResponse(TypedDict):
    flywheel_iteration_properties: NotRequired[
        "aws_sdk_comprehend.types.flywheel_iteration_properties.FlywheelIterationProperties"
    ]
    """<p>The configuration properties of a flywheel iteration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFlywheelIterationResponse) -> dict:
    out: dict = {}
    if "flywheel_iteration_properties" in value:
        import aws_sdk_comprehend.types.flywheel_iteration_properties

        out["FlywheelIterationProperties"] = (
            aws_sdk_comprehend.types.flywheel_iteration_properties.serialize_aws_json_1_1(
                value["flywheel_iteration_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFlywheelIterationResponse:
    out: DescribeFlywheelIterationResponse = {}  # type: ignore[typeddict-item]
    if "FlywheelIterationProperties" in data:
        import aws_sdk_comprehend.types.flywheel_iteration_properties

        out["flywheel_iteration_properties"] = (
            aws_sdk_comprehend.types.flywheel_iteration_properties.deserialize_aws_json_1_1(
                data["FlywheelIterationProperties"]
            )
        )
    return out

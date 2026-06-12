"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateFlywheelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.flywheel_properties


class UpdateFlywheelResponse(TypedDict):
    flywheel_properties: NotRequired[
        "aws_sdk_comprehend.types.flywheel_properties.FlywheelProperties"
    ]
    """<p>The flywheel properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFlywheelResponse) -> dict:
    out: dict = {}
    if "flywheel_properties" in value:
        import aws_sdk_comprehend.types.flywheel_properties

        out["FlywheelProperties"] = (
            aws_sdk_comprehend.types.flywheel_properties.serialize_aws_json_1_1(
                value["flywheel_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFlywheelResponse:
    out: UpdateFlywheelResponse = {}  # type: ignore[typeddict-item]
    if "FlywheelProperties" in data:
        import aws_sdk_comprehend.types.flywheel_properties

        out["flywheel_properties"] = (
            aws_sdk_comprehend.types.flywheel_properties.deserialize_aws_json_1_1(
                data["FlywheelProperties"]
            )
        )
    return out

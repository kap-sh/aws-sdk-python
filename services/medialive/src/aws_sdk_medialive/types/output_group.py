"""Generated from Smithy shape ``com.amazonaws.medialive#OutputGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_output
    import aws_sdk_medialive.types.__string_max32
    import aws_sdk_medialive.types.output_group_settings


class OutputGroup(TypedDict, closed=True):
    name: NotRequired["aws_sdk_medialive.types.__string_max32.__stringMax32"]
    """Custom output group name optionally defined by the user."""
    output_group_settings: NotRequired[
        "aws_sdk_medialive.types.output_group_settings.OutputGroupSettings"
    ]
    """Settings associated with the output group."""
    outputs: NotRequired["aws_sdk_medialive.types.__list_of_output.__listOfOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "output_group_settings" in value:
        import aws_sdk_medialive.types.output_group_settings

        out["outputGroupSettings"] = (
            aws_sdk_medialive.types.output_group_settings.serialize_json(
                value["output_group_settings"]
            )
        )
    if "outputs" in value:
        import aws_sdk_medialive.types.__list_of_output

        out["outputs"] = aws_sdk_medialive.types.__list_of_output.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> OutputGroup:
    out: OutputGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "outputGroupSettings" in data:
        import aws_sdk_medialive.types.output_group_settings

        out["output_group_settings"] = (
            aws_sdk_medialive.types.output_group_settings.deserialize_json(
                data["outputGroupSettings"]
            )
        )
    if "outputs" in data:
        import aws_sdk_medialive.types.__list_of_output

        out["outputs"] = aws_sdk_medialive.types.__list_of_output.deserialize_json(
            data["outputs"]
        )
    return out

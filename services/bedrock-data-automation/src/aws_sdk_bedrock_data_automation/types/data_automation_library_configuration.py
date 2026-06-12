"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_items


class DataAutomationLibraryConfiguration(TypedDict):
    libraries: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_items.DataAutomationLibraryItems"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryConfiguration) -> dict:
    out: dict = {}
    if "libraries" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_items

        out["libraries"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_items.serialize_json(
                value["libraries"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAutomationLibraryConfiguration:
    out: DataAutomationLibraryConfiguration = {}  # type: ignore[typeddict-item]
    if "libraries" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_items

        out["libraries"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_items.deserialize_json(
                data["libraries"]
            )
        )
    return out

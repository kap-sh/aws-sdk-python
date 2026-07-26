"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_item

DataAutomationLibraryItems: TypeAlias = list[
    "capo_bedrock_data_automation.types.data_automation_library_item.DataAutomationLibraryItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryItems) -> list:
    import capo_bedrock_data_automation.types.data_automation_library_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationLibraryItems:
    import capo_bedrock_data_automation.types.data_automation_library_item

    out: DataAutomationLibraryItems = []
    for item in data:
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_item.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationLibraryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library


class GetDataAutomationLibraryResponse(TypedDict, closed=True):
    library: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library.DataAutomationLibrary"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationLibraryResponse) -> dict:
    out: dict = {}
    if "library" in value:
        import capo_bedrock_data_automation.types.data_automation_library

        out["library"] = (
            capo_bedrock_data_automation.types.data_automation_library.serialize_json(
                value["library"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataAutomationLibraryResponse:
    out: GetDataAutomationLibraryResponse = {}  # type: ignore[typeddict-item]
    if "library" in data:
        import capo_bedrock_data_automation.types.data_automation_library

        out["library"] = (
            capo_bedrock_data_automation.types.data_automation_library.deserialize_json(
                data["library"]
            )
        )
    return out

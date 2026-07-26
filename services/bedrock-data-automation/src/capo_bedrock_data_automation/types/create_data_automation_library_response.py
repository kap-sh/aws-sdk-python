"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateDataAutomationLibraryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.data_automation_library_status


class CreateDataAutomationLibraryResponse(TypedDict, closed=True):
    library_arn: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    ]
    status: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_status.DataAutomationLibraryStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAutomationLibraryResponse) -> dict:
    out: dict = {}
    if "library_arn" in value:
        out["libraryArn"] = value["library_arn"]
    if "status" in value:
        import capo_bedrock_data_automation.types.data_automation_library_status

        out["status"] = (
            capo_bedrock_data_automation.types.data_automation_library_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataAutomationLibraryResponse:
    out: CreateDataAutomationLibraryResponse = {}  # type: ignore[typeddict-item]
    if "libraryArn" in data:
        out["library_arn"] = data["libraryArn"]
    if "status" in data:
        import capo_bedrock_data_automation.types.data_automation_library_status

        out["status"] = (
            capo_bedrock_data_automation.types.data_automation_library_status.deserialize_json(
                data["status"]
            )
        )
    return out

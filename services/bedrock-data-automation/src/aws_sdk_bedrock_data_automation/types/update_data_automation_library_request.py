"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateDataAutomationLibraryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_library_description


class UpdateDataAutomationLibraryRequest(TypedDict, closed=True):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""
    library_description: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
    ]
    client_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataAutomationLibraryRequest) -> dict:
    out: dict = {}
    if "library_description" in value:
        out["libraryDescription"] = value["library_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateDataAutomationLibraryRequest:
    out: UpdateDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
    if "libraryDescription" in data:
        out["library_description"] = data["libraryDescription"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

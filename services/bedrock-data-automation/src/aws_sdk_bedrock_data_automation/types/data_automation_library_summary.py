"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibrarySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_library_name
    import aws_sdk_bedrock_data_automation.types.date_timestamp


class DataAutomationLibrarySummary(TypedDict):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    library_name: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName"
    ]
    creation_time: "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibrarySummary) -> dict:
    out: dict = {}
    out["libraryArn"] = value["library_arn"]
    if "library_name" in value:
        out["libraryName"] = value["library_name"]
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataAutomationLibrarySummary:
    out: DataAutomationLibrarySummary = {}  # type: ignore[typeddict-item]
    if "libraryArn" in data:
        out["library_arn"] = data["libraryArn"]
    else:
        raise DeserializationError("DataAutomationLibrarySummary.library_arn required")
    if "libraryName" in data:
        out["library_name"] = data["libraryName"]
    if "creationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationLibrarySummary.creation_time required"
        )
    return out

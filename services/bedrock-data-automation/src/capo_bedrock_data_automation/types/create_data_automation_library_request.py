"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateDataAutomationLibraryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.data_automation_library_description
    import capo_bedrock_data_automation.types.data_automation_library_name
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.tag_list


class CreateDataAutomationLibraryRequest(TypedDict, closed=True):
    library_name: "capo_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName"
    library_description: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
    ]
    client_token: NotRequired[
        "capo_bedrock_data_automation.types.client_token.ClientToken"
    ]
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]
    tags: NotRequired["capo_bedrock_data_automation.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAutomationLibraryRequest) -> dict:
    out: dict = {}
    out["libraryName"] = value["library_name"]
    if "library_description" in value:
        out["libraryDescription"] = value["library_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "encryption_configuration" in value:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataAutomationLibraryRequest:
    out: CreateDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
    if "libraryName" in data:
        out["library_name"] = data["libraryName"]
    else:
        raise DeserializationError(
            "CreateDataAutomationLibraryRequest.library_name required"
        )
    if "libraryDescription" in data:
        out["library_description"] = data["libraryDescription"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "encryptionConfiguration" in data:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if "tags" in data:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibrary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_library_description
    import aws_sdk_bedrock_data_automation.types.data_automation_library_name
    import aws_sdk_bedrock_data_automation.types.data_automation_library_status
    import aws_sdk_bedrock_data_automation.types.date_timestamp
    import aws_sdk_bedrock_data_automation.types.entity_type_info_list
    import aws_sdk_bedrock_data_automation.types.kms_encryption_context
    import aws_sdk_bedrock_data_automation.types.kms_key_id


class DataAutomationLibrary(TypedDict, closed=True):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    creation_time: "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    library_name: "aws_sdk_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName"
    library_description: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
    ]
    status: "aws_sdk_bedrock_data_automation.types.data_automation_library_status.DataAutomationLibraryStatus"
    entity_types: NotRequired[
        "aws_sdk_bedrock_data_automation.types.entity_type_info_list.EntityTypeInfoList"
    ]
    kms_key_id: NotRequired["aws_sdk_bedrock_data_automation.types.kms_key_id.KmsKeyId"]
    kms_encryption_context: NotRequired[
        "aws_sdk_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibrary) -> dict:
    out: dict = {}
    out["libraryArn"] = value["library_arn"]
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["libraryName"] = value["library_name"]
    if "library_description" in value:
        out["libraryDescription"] = value["library_description"]
    import aws_sdk_bedrock_data_automation.types.data_automation_library_status

    out["status"] = (
        aws_sdk_bedrock_data_automation.types.data_automation_library_status.serialize_json(
            value["status"]
        )
    )
    if "entity_types" in value:
        import aws_sdk_bedrock_data_automation.types.entity_type_info_list

        out["entityTypes"] = (
            aws_sdk_bedrock_data_automation.types.entity_type_info_list.serialize_json(
                value["entity_types"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "kms_encryption_context" in value:
        import aws_sdk_bedrock_data_automation.types.kms_encryption_context

        out["kmsEncryptionContext"] = (
            aws_sdk_bedrock_data_automation.types.kms_encryption_context.serialize_json(
                value["kms_encryption_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAutomationLibrary:
    out: DataAutomationLibrary = {}  # type: ignore[typeddict-item]
    if "libraryArn" in data:
        out["library_arn"] = data["libraryArn"]
    else:
        raise DeserializationError("DataAutomationLibrary.library_arn required")
    if "creationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("DataAutomationLibrary.creation_time required")
    if "libraryName" in data:
        out["library_name"] = data["libraryName"]
    else:
        raise DeserializationError("DataAutomationLibrary.library_name required")
    if "libraryDescription" in data:
        out["library_description"] = data["libraryDescription"]
    if "status" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_status

        out["status"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DataAutomationLibrary.status required")
    if "entityTypes" in data:
        import aws_sdk_bedrock_data_automation.types.entity_type_info_list

        out["entity_types"] = (
            aws_sdk_bedrock_data_automation.types.entity_type_info_list.deserialize_json(
                data["entityTypes"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "kmsEncryptionContext" in data:
        import aws_sdk_bedrock_data_automation.types.kms_encryption_context

        out["kms_encryption_context"] = (
            aws_sdk_bedrock_data_automation.types.kms_encryption_context.deserialize_json(
                data["kmsEncryptionContext"]
            )
        )
    return out

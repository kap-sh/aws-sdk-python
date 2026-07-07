"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Blueprint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_name
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples
    import aws_sdk_bedrock_data_automation.types.blueprint_schema
    import aws_sdk_bedrock_data_automation.types.blueprint_stage
    import aws_sdk_bedrock_data_automation.types.blueprint_version
    import aws_sdk_bedrock_data_automation.types.date_timestamp
    import aws_sdk_bedrock_data_automation.types.kms_encryption_context
    import aws_sdk_bedrock_data_automation.types.kms_key_id
    import aws_sdk_bedrock_data_automation.types.type


class Blueprint(TypedDict, closed=True):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    schema: "aws_sdk_bedrock_data_automation.types.blueprint_schema.BlueprintSchema"
    type: "aws_sdk_bedrock_data_automation.types.type.Type"
    creation_time: "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    last_modified_time: (
        "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    )
    blueprint_name: "aws_sdk_bedrock_data_automation.types.blueprint_name.BlueprintName"
    blueprint_version: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    blueprint_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    kms_key_id: NotRequired["aws_sdk_bedrock_data_automation.types.kms_key_id.KmsKeyId"]
    kms_encryption_context: NotRequired[
        "aws_sdk_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]
    optimization_samples: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples"
    ]
    optimization_time: NotRequired[
        "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Blueprint) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    out["schema"] = value["schema"]
    import aws_sdk_bedrock_data_automation.types.type

    out["type"] = aws_sdk_bedrock_data_automation.types.type.serialize_json(
        value["type"]
    )
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["lastModifiedTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["blueprintName"] = value["blueprint_name"]
    if "blueprint_version" in value:
        out["blueprintVersion"] = value["blueprint_version"]
    if "blueprint_stage" in value:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
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
    if "optimization_samples" in value:
        import aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples

        out["optimizationSamples"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples.serialize_json(
                value["optimization_samples"]
            )
        )
    if "optimization_time" in value:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["optimizationTime"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["optimization_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> Blueprint:
    out: Blueprint = {}  # type: ignore[typeddict-item]
    if "blueprintArn" in data:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        raise DeserializationError("Blueprint.blueprint_arn required")
    if "schema" in data:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("Blueprint.schema required")
    if "type" in data:
        import aws_sdk_bedrock_data_automation.types.type

        out["type"] = aws_sdk_bedrock_data_automation.types.type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("Blueprint.type required")
    if "creationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("Blueprint.creation_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("Blueprint.last_modified_time required")
    if "blueprintName" in data:
        out["blueprint_name"] = data["blueprintName"]
    else:
        raise DeserializationError("Blueprint.blueprint_name required")
    if "blueprintVersion" in data:
        out["blueprint_version"] = data["blueprintVersion"]
    if "blueprintStage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
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
    if "optimizationSamples" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples

        out["optimization_samples"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples.deserialize_json(
                data["optimizationSamples"]
            )
        )
    if "optimizationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["optimization_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["optimizationTime"]
            )
        )
    return out

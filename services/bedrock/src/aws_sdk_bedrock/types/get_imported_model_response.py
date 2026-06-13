"""Generated from Smithy shape ``com.amazonaws.bedrock#GetImportedModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_units
    import aws_sdk_bedrock.types.imported_model_arn
    import aws_sdk_bedrock.types.imported_model_name
    import aws_sdk_bedrock.types.instruct_supported
    import aws_sdk_bedrock.types.job_name
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.model_data_source
    import aws_sdk_bedrock.types.model_import_job_arn
    import aws_sdk_bedrock.types.timestamp


class GetImportedModelResponse(TypedDict):
    model_arn: NotRequired["aws_sdk_bedrock.types.imported_model_arn.ImportedModelArn"]
    """<p>The Amazon Resource Name (ARN) associated with this imported model.</p>"""
    model_name: NotRequired[
        "aws_sdk_bedrock.types.imported_model_name.ImportedModelName"
    ]
    """<p>The name of the imported model.</p>"""
    job_name: NotRequired["aws_sdk_bedrock.types.job_name.JobName"]
    """<p>Job name associated with the imported model.</p>"""
    job_arn: NotRequired["aws_sdk_bedrock.types.model_import_job_arn.ModelImportJobArn"]
    """<p>Job Amazon Resource Name (ARN) associated with the imported model.</p>"""
    model_data_source: NotRequired[
        "aws_sdk_bedrock.types.model_data_source.ModelDataSource"
    ]
    """<p>The data source for this imported model.</p>"""
    creation_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Creation time of the imported model.</p>"""
    model_architecture: NotRequired["str"]
    """<p>The architecture of the imported model.</p>"""
    model_kms_key_arn: NotRequired["aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The imported model is encrypted at rest using this key.</p>"""
    instruct_supported: NotRequired[
        "aws_sdk_bedrock.types.instruct_supported.InstructSupported"
    ]
    """<p>Specifies if the imported model supports converse.</p>"""
    custom_model_units: NotRequired[
        "aws_sdk_bedrock.types.custom_model_units.CustomModelUnits"
    ]
    """<p>Information about the hardware utilization for a single copy of the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportedModelResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["modelArn"] = value["model_arn"]
    if "model_name" in value:
        out["modelName"] = value["model_name"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "model_data_source" in value:
        import aws_sdk_bedrock.types.model_data_source

        out["modelDataSource"] = aws_sdk_bedrock.types.model_data_source.serialize_json(
            value["model_data_source"]
        )
    if "creation_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "model_architecture" in value:
        out["modelArchitecture"] = value["model_architecture"]
    if "model_kms_key_arn" in value:
        out["modelKmsKeyArn"] = value["model_kms_key_arn"]
    if "instruct_supported" in value:
        out["instructSupported"] = value["instruct_supported"]
    if "custom_model_units" in value:
        import aws_sdk_bedrock.types.custom_model_units

        out["customModelUnits"] = (
            aws_sdk_bedrock.types.custom_model_units.serialize_json(
                value["custom_model_units"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetImportedModelResponse:
    out: GetImportedModelResponse = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    if "modelName" in data:
        out["model_name"] = data["modelName"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "modelDataSource" in data:
        import aws_sdk_bedrock.types.model_data_source

        out["model_data_source"] = (
            aws_sdk_bedrock.types.model_data_source.deserialize_json(
                data["modelDataSource"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "modelArchitecture" in data:
        out["model_architecture"] = data["modelArchitecture"]
    if "modelKmsKeyArn" in data:
        out["model_kms_key_arn"] = data["modelKmsKeyArn"]
    if "instructSupported" in data:
        out["instruct_supported"] = data["instructSupported"]
    if "customModelUnits" in data:
        import aws_sdk_bedrock.types.custom_model_units

        out["custom_model_units"] = (
            aws_sdk_bedrock.types.custom_model_units.deserialize_json(
                data["customModelUnits"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#AthenaDatasetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.athena_catalog
    import capo_sagemaker.types.athena_database
    import capo_sagemaker.types.athena_query_string
    import capo_sagemaker.types.athena_result_compression_type
    import capo_sagemaker.types.athena_result_format
    import capo_sagemaker.types.athena_work_group
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.s3_uri


class AthenaDatasetDefinition(TypedDict, closed=True):
    catalog: NotRequired["capo_sagemaker.types.athena_catalog.AthenaCatalog"]
    database: NotRequired["capo_sagemaker.types.athena_database.AthenaDatabase"]
    query_string: NotRequired[
        "capo_sagemaker.types.athena_query_string.AthenaQueryString"
    ]
    work_group: NotRequired["capo_sagemaker.types.athena_work_group.AthenaWorkGroup"]
    output_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The location in Amazon S3 where Athena query results are stored.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data generated from an Athena query execution.</p>"""
    output_format: NotRequired[
        "capo_sagemaker.types.athena_result_format.AthenaResultFormat"
    ]
    output_compression: NotRequired[
        "capo_sagemaker.types.athena_result_compression_type.AthenaResultCompressionType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AthenaDatasetDefinition) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "database" in value:
        out["Database"] = value["database"]
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    if "output_s3_uri" in value:
        out["OutputS3Uri"] = value["output_s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "output_format" in value:
        import capo_sagemaker.types.athena_result_format

        out["OutputFormat"] = (
            capo_sagemaker.types.athena_result_format.serialize_aws_json_1_1(
                value["output_format"]
            )
        )
    if "output_compression" in value:
        import capo_sagemaker.types.athena_result_compression_type

        out["OutputCompression"] = (
            capo_sagemaker.types.athena_result_compression_type.serialize_aws_json_1_1(
                value["output_compression"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AthenaDatasetDefinition:
    out: AthenaDatasetDefinition = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    if "Database" in data:
        out["database"] = data["Database"]
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    if "OutputS3Uri" in data:
        out["output_s3_uri"] = data["OutputS3Uri"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "OutputFormat" in data:
        import capo_sagemaker.types.athena_result_format

        out["output_format"] = (
            capo_sagemaker.types.athena_result_format.deserialize_aws_json_1_1(
                data["OutputFormat"]
            )
        )
    if "OutputCompression" in data:
        import capo_sagemaker.types.athena_result_compression_type

        out["output_compression"] = (
            capo_sagemaker.types.athena_result_compression_type.deserialize_aws_json_1_1(
                data["OutputCompression"]
            )
        )
    return out

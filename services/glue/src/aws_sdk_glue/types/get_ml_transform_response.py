"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTransformResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.evaluation_metrics
    import aws_sdk_glue.types.glue_tables
    import aws_sdk_glue.types.glue_version_string
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.label_count
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_double
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.role_string
    import aws_sdk_glue.types.timeout
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.transform_encryption
    import aws_sdk_glue.types.transform_parameters
    import aws_sdk_glue.types.transform_schema
    import aws_sdk_glue.types.transform_status_type
    import aws_sdk_glue.types.worker_type


class GetMLTransformResponse(TypedDict):
    transform_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique identifier of the transform, generated at the time that the transform was created.</p>"""
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The unique name given to the transform when it was created.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the transform.</p>"""
    status: NotRequired["aws_sdk_glue.types.transform_status_type.TransformStatusType"]
    r"""<p>The last known status of the transform (to indicate whether it can be used or not). One of \"NOT_READY\", \"READY\", or \"DELETING\".</p>"""
    created_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time when the transform was created.</p>"""
    last_modified_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time when the transform was last modified.</p>"""
    input_record_tables: NotRequired["aws_sdk_glue.types.glue_tables.GlueTables"]
    """<p>A list of Glue table definitions used by the transform.</p>"""
    parameters: NotRequired[
        "aws_sdk_glue.types.transform_parameters.TransformParameters"
    ]
    """<p>The configuration parameters that are specific to the algorithm used.</p>"""
    evaluation_metrics: NotRequired[
        "aws_sdk_glue.types.evaluation_metrics.EvaluationMetrics"
    ]
    """<p>The latest evaluation metrics.</p>"""
    label_count: "aws_sdk_glue.types.label_count.LabelCount"
    """<p>The number of labels available for this transform.</p>"""
    schema: NotRequired["aws_sdk_glue.types.transform_schema.TransformSchema"]
    """<p>The <code>Map<Column, Type></code> object that represents the schema that this transform accepts. Has an upper bound of 100 columns.</p>"""
    role: NotRequired["aws_sdk_glue.types.role_string.RoleString"]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.</p>"""
    glue_version: NotRequired[
        "aws_sdk_glue.types.glue_version_string.GlueVersionString"
    ]
    r"""<p>This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions\">Glue Versions</a> in the developer guide.</p>"""
    max_capacity: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    r"""<p>The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href=\"https://aws.amazon.com/glue/pricing/\">Glue pricing page</a>. </p> <p>When the <code>WorkerType</code> field is set to a value other than <code>Standard</code>, the <code>MaxCapacity</code> field is set automatically and becomes read-only.</p>"""
    worker_type: NotRequired["aws_sdk_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.</p> <ul> <li> <p>For the <code>Standard</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.</p> </li> <li> <p>For the <code>G.1X</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.</p> </li> </ul>"""
    number_of_workers: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated when this task runs.</p>"""
    timeout: NotRequired["aws_sdk_glue.types.timeout.Timeout"]
    """<p>The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    max_retries: NotRequired["aws_sdk_glue.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of times to retry a task for this transform after a task run fails.</p>"""
    transform_encryption: NotRequired[
        "aws_sdk_glue.types.transform_encryption.TransformEncryption"
    ]
    """<p>The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTransformResponse) -> dict:
    out: dict = {}
    if "transform_id" in value:
        out["TransformId"] = value["transform_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_glue.types.transform_status_type

        out["Status"] = aws_sdk_glue.types.transform_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_on" in value:
        import aws_sdk_glue.types.timestamp

        out["CreatedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "last_modified_on" in value:
        import aws_sdk_glue.types.timestamp

        out["LastModifiedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    if "input_record_tables" in value:
        import aws_sdk_glue.types.glue_tables

        out["InputRecordTables"] = (
            aws_sdk_glue.types.glue_tables.serialize_aws_json_1_1(
                value["input_record_tables"]
            )
        )
    if "parameters" in value:
        import aws_sdk_glue.types.transform_parameters

        out["Parameters"] = (
            aws_sdk_glue.types.transform_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "evaluation_metrics" in value:
        import aws_sdk_glue.types.evaluation_metrics

        out["EvaluationMetrics"] = (
            aws_sdk_glue.types.evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    out["LabelCount"] = value.get("label_count", 0)
    if "schema" in value:
        import aws_sdk_glue.types.transform_schema

        out["Schema"] = aws_sdk_glue.types.transform_schema.serialize_aws_json_1_1(
            value["schema"]
        )
    if "role" in value:
        out["Role"] = value["role"]
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "worker_type" in value:
        import aws_sdk_glue.types.worker_type

        out["WorkerType"] = aws_sdk_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "max_retries" in value:
        out["MaxRetries"] = value["max_retries"]
    if "transform_encryption" in value:
        import aws_sdk_glue.types.transform_encryption

        out["TransformEncryption"] = (
            aws_sdk_glue.types.transform_encryption.serialize_aws_json_1_1(
                value["transform_encryption"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTransformResponse:
    out: GetMLTransformResponse = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_glue.types.transform_status_type

        out["status"] = (
            aws_sdk_glue.types.transform_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreatedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["created_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if "LastModifiedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["last_modified_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedOn"]
        )
    if "InputRecordTables" in data:
        import aws_sdk_glue.types.glue_tables

        out["input_record_tables"] = (
            aws_sdk_glue.types.glue_tables.deserialize_aws_json_1_1(
                data["InputRecordTables"]
            )
        )
    if "Parameters" in data:
        import aws_sdk_glue.types.transform_parameters

        out["parameters"] = (
            aws_sdk_glue.types.transform_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if "EvaluationMetrics" in data:
        import aws_sdk_glue.types.evaluation_metrics

        out["evaluation_metrics"] = (
            aws_sdk_glue.types.evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    if "LabelCount" in data:
        out["label_count"] = data["LabelCount"]
    else:
        out["label_count"] = 0
    if "Schema" in data:
        import aws_sdk_glue.types.transform_schema

        out["schema"] = aws_sdk_glue.types.transform_schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    if "Role" in data:
        out["role"] = data["Role"]
    if "GlueVersion" in data:
        out["glue_version"] = data["GlueVersion"]
    if "MaxCapacity" in data:
        out["max_capacity"] = data["MaxCapacity"]
    if "WorkerType" in data:
        import aws_sdk_glue.types.worker_type

        out["worker_type"] = aws_sdk_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "MaxRetries" in data:
        out["max_retries"] = data["MaxRetries"]
    if "TransformEncryption" in data:
        import aws_sdk_glue.types.transform_encryption

        out["transform_encryption"] = (
            aws_sdk_glue.types.transform_encryption.deserialize_aws_json_1_1(
                data["TransformEncryption"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#Job``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.account_id
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.data_catalog_output_list
    import aws_sdk_databrew.types.database_output_list
    import aws_sdk_databrew.types.dataset_name
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.encryption_key_arn
    import aws_sdk_databrew.types.encryption_mode
    import aws_sdk_databrew.types.job_name
    import aws_sdk_databrew.types.job_sample
    import aws_sdk_databrew.types.job_type
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.log_subscription
    import aws_sdk_databrew.types.max_capacity
    import aws_sdk_databrew.types.max_retries
    import aws_sdk_databrew.types.output_list
    import aws_sdk_databrew.types.project_name
    import aws_sdk_databrew.types.recipe_reference
    import aws_sdk_databrew.types.tag_map
    import aws_sdk_databrew.types.timeout
    import aws_sdk_databrew.types.validation_configuration_list


class Job(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_databrew.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the job.</p>"""
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the job.</p>"""
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the job was created.</p>"""
    dataset_name: NotRequired["aws_sdk_databrew.types.dataset_name.DatasetName"]
    """<p>A dataset that the job is to process.</p>"""
    encryption_key_arn: NotRequired[
        "aws_sdk_databrew.types.encryption_key_arn.EncryptionKeyArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job output. For more information, see <a href=\"https://docs.aws.amazon.com/databrew/latest/dg/encryption-security-configuration.html\">Encrypting data written by DataBrew jobs</a> </p>"""
    encryption_mode: NotRequired[
        "aws_sdk_databrew.types.encryption_mode.EncryptionMode"
    ]
    """<p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - Server-side encryption with keys managed by KMS.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>"""
    name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The unique name of the job.</p>"""
    type: NotRequired["aws_sdk_databrew.types.job_type.JobType"]
    """<p>The job type of the job, which must be one of the following:</p> <ul> <li> <p> <code>PROFILE</code> - A job to analyze a dataset, to determine its size, data types, data distribution, and more.</p> </li> <li> <p> <code>RECIPE</code> - A job to apply one or more transformations to a dataset.</p> </li> </ul>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the job.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The modification date and time of the job.</p>"""
    log_subscription: NotRequired[
        "aws_sdk_databrew.types.log_subscription.LogSubscription"
    ]
    """<p>The current status of Amazon CloudWatch logging for the job.</p>"""
    max_capacity: "aws_sdk_databrew.types.max_capacity.MaxCapacity"
    """<p>The maximum number of nodes that can be consumed when the job processes data.</p>"""
    max_retries: "aws_sdk_databrew.types.max_retries.MaxRetries"
    """<p>The maximum number of times to retry the job after a job run fails.</p>"""
    outputs: NotRequired["aws_sdk_databrew.types.output_list.OutputList"]
    """<p>One or more artifacts that represent output from running the job.</p>"""
    data_catalog_outputs: NotRequired[
        "aws_sdk_databrew.types.data_catalog_output_list.DataCatalogOutputList"
    ]
    """<p>One or more artifacts that represent the Glue Data Catalog output from running the job.</p>"""
    database_outputs: NotRequired[
        "aws_sdk_databrew.types.database_output_list.DatabaseOutputList"
    ]
    """<p>Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.</p>"""
    project_name: NotRequired["aws_sdk_databrew.types.project_name.ProjectName"]
    """<p>The name of the project that the job is associated with.</p>"""
    recipe_reference: NotRequired[
        "aws_sdk_databrew.types.recipe_reference.RecipeReference"
    ]
    """<p>A set of steps that the job runs.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The unique Amazon Resource Name (ARN) for the job.</p>"""
    role_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the role to be assumed for this job.</p>"""
    timeout: "aws_sdk_databrew.types.timeout.Timeout"
    """<p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the job.</p>"""
    job_sample: NotRequired["aws_sdk_databrew.types.job_sample.JobSample"]
    """<p>A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a <code>JobSample</code> value isn't provided, the default value is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.</p>"""
    validation_configurations: NotRequired[
        "aws_sdk_databrew.types.validation_configuration_list.ValidationConfigurationList"
    ]
    """<p>List of validation configurations that are applied to the profile job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "encryption_mode" in value:
        import aws_sdk_databrew.types.encryption_mode

        out["EncryptionMode"] = aws_sdk_databrew.types.encryption_mode.serialize_json(
            value["encryption_mode"]
        )
    out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_databrew.types.job_type

        out["Type"] = aws_sdk_databrew.types.job_type.serialize_json(value["type"])
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "log_subscription" in value:
        import aws_sdk_databrew.types.log_subscription

        out["LogSubscription"] = aws_sdk_databrew.types.log_subscription.serialize_json(
            value["log_subscription"]
        )
    out["MaxCapacity"] = value.get("max_capacity", 0)
    out["MaxRetries"] = value.get("max_retries", 0)
    if "outputs" in value:
        import aws_sdk_databrew.types.output_list

        out["Outputs"] = aws_sdk_databrew.types.output_list.serialize_json(
            value["outputs"]
        )
    if "data_catalog_outputs" in value:
        import aws_sdk_databrew.types.data_catalog_output_list

        out["DataCatalogOutputs"] = (
            aws_sdk_databrew.types.data_catalog_output_list.serialize_json(
                value["data_catalog_outputs"]
            )
        )
    if "database_outputs" in value:
        import aws_sdk_databrew.types.database_output_list

        out["DatabaseOutputs"] = (
            aws_sdk_databrew.types.database_output_list.serialize_json(
                value["database_outputs"]
            )
        )
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "recipe_reference" in value:
        import aws_sdk_databrew.types.recipe_reference

        out["RecipeReference"] = aws_sdk_databrew.types.recipe_reference.serialize_json(
            value["recipe_reference"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    out["Timeout"] = value.get("timeout", 0)
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    if "job_sample" in value:
        import aws_sdk_databrew.types.job_sample

        out["JobSample"] = aws_sdk_databrew.types.job_sample.serialize_json(
            value["job_sample"]
        )
    if "validation_configurations" in value:
        import aws_sdk_databrew.types.validation_configuration_list

        out["ValidationConfigurations"] = (
            aws_sdk_databrew.types.validation_configuration_list.serialize_json(
                value["validation_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "EncryptionMode" in data:
        import aws_sdk_databrew.types.encryption_mode

        out["encryption_mode"] = (
            aws_sdk_databrew.types.encryption_mode.deserialize_json(
                data["EncryptionMode"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Job.name required")
    if "Type" in data:
        import aws_sdk_databrew.types.job_type

        out["type"] = aws_sdk_databrew.types.job_type.deserialize_json(data["Type"])
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "LogSubscription" in data:
        import aws_sdk_databrew.types.log_subscription

        out["log_subscription"] = (
            aws_sdk_databrew.types.log_subscription.deserialize_json(
                data["LogSubscription"]
            )
        )
    if "MaxCapacity" in data:
        out["max_capacity"] = data["MaxCapacity"]
    else:
        out["max_capacity"] = 0
    if "MaxRetries" in data:
        out["max_retries"] = data["MaxRetries"]
    else:
        out["max_retries"] = 0
    if "Outputs" in data:
        import aws_sdk_databrew.types.output_list

        out["outputs"] = aws_sdk_databrew.types.output_list.deserialize_json(
            data["Outputs"]
        )
    if "DataCatalogOutputs" in data:
        import aws_sdk_databrew.types.data_catalog_output_list

        out["data_catalog_outputs"] = (
            aws_sdk_databrew.types.data_catalog_output_list.deserialize_json(
                data["DataCatalogOutputs"]
            )
        )
    if "DatabaseOutputs" in data:
        import aws_sdk_databrew.types.database_output_list

        out["database_outputs"] = (
            aws_sdk_databrew.types.database_output_list.deserialize_json(
                data["DatabaseOutputs"]
            )
        )
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    if "RecipeReference" in data:
        import aws_sdk_databrew.types.recipe_reference

        out["recipe_reference"] = (
            aws_sdk_databrew.types.recipe_reference.deserialize_json(
                data["RecipeReference"]
            )
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    else:
        out["timeout"] = 0
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "JobSample" in data:
        import aws_sdk_databrew.types.job_sample

        out["job_sample"] = aws_sdk_databrew.types.job_sample.deserialize_json(
            data["JobSample"]
        )
    if "ValidationConfigurations" in data:
        import aws_sdk_databrew.types.validation_configuration_list

        out["validation_configurations"] = (
            aws_sdk_databrew.types.validation_configuration_list.deserialize_json(
                data["ValidationConfigurations"]
            )
        )
    return out

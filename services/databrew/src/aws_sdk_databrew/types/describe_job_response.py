"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
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
    import aws_sdk_databrew.types.profile_configuration
    import aws_sdk_databrew.types.project_name
    import aws_sdk_databrew.types.recipe_reference
    import aws_sdk_databrew.types.tag_map
    import aws_sdk_databrew.types.timeout
    import aws_sdk_databrew.types.validation_configuration_list


class DescribeJobResponse(TypedDict):
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the job was created.</p>"""
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The identifier (user name) of the user associated with the creation of the job.</p>"""
    dataset_name: NotRequired["aws_sdk_databrew.types.dataset_name.DatasetName"]
    """<p>The dataset that the job acts upon.</p>"""
    encryption_key_arn: NotRequired[
        "aws_sdk_databrew.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.</p>"""
    encryption_mode: NotRequired[
        "aws_sdk_databrew.types.encryption_mode.EncryptionMode"
    ]
    """<p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - Server-side encryption with keys managed by KMS.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>"""
    name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The name of the job.</p>"""
    type: NotRequired["aws_sdk_databrew.types.job_type.JobType"]
    """<p>The job type, which must be one of the following:</p> <ul> <li> <p> <code>PROFILE</code> - The job analyzes the dataset to determine its size, data types, data distribution, and more.</p> </li> <li> <p> <code>RECIPE</code> - The job applies one or more transformations to a dataset.</p> </li> </ul>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The identifier (user name) of the user who last modified the job.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the job was last modified.</p>"""
    log_subscription: NotRequired[
        "aws_sdk_databrew.types.log_subscription.LogSubscription"
    ]
    """<p>Indicates whether Amazon CloudWatch logging is enabled for this job.</p>"""
    max_capacity: "aws_sdk_databrew.types.max_capacity.MaxCapacity"
    """<p>The maximum number of compute nodes that DataBrew can consume when the job processes data.</p>"""
    max_retries: "aws_sdk_databrew.types.max_retries.MaxRetries"
    """<p>The maximum number of times to retry the job after a job run fails.</p>"""
    outputs: NotRequired["aws_sdk_databrew.types.output_list.OutputList"]
    """<p>One or more artifacts that represent the output from running the job.</p>"""
    data_catalog_outputs: NotRequired[
        "aws_sdk_databrew.types.data_catalog_output_list.DataCatalogOutputList"
    ]
    """<p>One or more artifacts that represent the Glue Data Catalog output from running the job.</p>"""
    database_outputs: NotRequired[
        "aws_sdk_databrew.types.database_output_list.DatabaseOutputList"
    ]
    """<p>Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.</p>"""
    project_name: NotRequired["aws_sdk_databrew.types.project_name.ProjectName"]
    """<p>The DataBrew project associated with this job.</p>"""
    profile_configuration: NotRequired[
        "aws_sdk_databrew.types.profile_configuration.ProfileConfiguration"
    ]
    """<p>Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.</p>"""
    validation_configurations: NotRequired[
        "aws_sdk_databrew.types.validation_configuration_list.ValidationConfigurationList"
    ]
    """<p>List of validation configurations that are applied to the profile job.</p>"""
    recipe_reference: NotRequired[
        "aws_sdk_databrew.types.recipe_reference.RecipeReference"
    ]
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    role_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The ARN of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags associated with this job.</p>"""
    timeout: "aws_sdk_databrew.types.timeout.Timeout"
    """<p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>"""
    job_sample: NotRequired["aws_sdk_databrew.types.job_sample.JobSample"]
    """<p>Sample configuration for profile jobs only. Determines the number of rows on which the profile job will be executed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobResponse) -> dict:
    out: dict = {}
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
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
    if "profile_configuration" in value:
        import aws_sdk_databrew.types.profile_configuration

        out["ProfileConfiguration"] = (
            aws_sdk_databrew.types.profile_configuration.serialize_json(
                value["profile_configuration"]
            )
        )
    if "validation_configurations" in value:
        import aws_sdk_databrew.types.validation_configuration_list

        out["ValidationConfigurations"] = (
            aws_sdk_databrew.types.validation_configuration_list.serialize_json(
                value["validation_configurations"]
            )
        )
    if "recipe_reference" in value:
        import aws_sdk_databrew.types.recipe_reference

        out["RecipeReference"] = aws_sdk_databrew.types.recipe_reference.serialize_json(
            value["recipe_reference"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    out["Timeout"] = value.get("timeout", 0)
    if "job_sample" in value:
        import aws_sdk_databrew.types.job_sample

        out["JobSample"] = aws_sdk_databrew.types.job_sample.serialize_json(
            value["job_sample"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobResponse:
    out: DescribeJobResponse = {}  # type: ignore[typeddict-item]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
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
        raise DeserializationError("DescribeJobResponse.name required")
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
    if "ProfileConfiguration" in data:
        import aws_sdk_databrew.types.profile_configuration

        out["profile_configuration"] = (
            aws_sdk_databrew.types.profile_configuration.deserialize_json(
                data["ProfileConfiguration"]
            )
        )
    if "ValidationConfigurations" in data:
        import aws_sdk_databrew.types.validation_configuration_list

        out["validation_configurations"] = (
            aws_sdk_databrew.types.validation_configuration_list.deserialize_json(
                data["ValidationConfigurations"]
            )
        )
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
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    else:
        out["timeout"] = 0
    if "JobSample" in data:
        import aws_sdk_databrew.types.job_sample

        out["job_sample"] = aws_sdk_databrew.types.job_sample.deserialize_json(
            data["JobSample"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeJobRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.attempt
    import aws_sdk_databrew.types.data_catalog_output_list
    import aws_sdk_databrew.types.database_output_list
    import aws_sdk_databrew.types.dataset_name
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.execution_time
    import aws_sdk_databrew.types.job_name
    import aws_sdk_databrew.types.job_run_error_message
    import aws_sdk_databrew.types.job_run_id
    import aws_sdk_databrew.types.job_run_state
    import aws_sdk_databrew.types.job_sample
    import aws_sdk_databrew.types.log_group_name
    import aws_sdk_databrew.types.log_subscription
    import aws_sdk_databrew.types.output_list
    import aws_sdk_databrew.types.profile_configuration
    import aws_sdk_databrew.types.recipe_reference
    import aws_sdk_databrew.types.started_by
    import aws_sdk_databrew.types.validation_configuration_list


class DescribeJobRunResponse(TypedDict):
    attempt: "aws_sdk_databrew.types.attempt.Attempt"
    """<p>The number of times that DataBrew has attempted to run the job.</p>"""
    completed_on: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time when the job completed processing.</p>"""
    dataset_name: NotRequired["aws_sdk_databrew.types.dataset_name.DatasetName"]
    """<p>The name of the dataset for the job to process.</p>"""
    error_message: NotRequired[
        "aws_sdk_databrew.types.job_run_error_message.JobRunErrorMessage"
    ]
    """<p>A message indicating an error (if any) that was encountered when the job ran.</p>"""
    execution_time: "aws_sdk_databrew.types.execution_time.ExecutionTime"
    """<p>The amount of time, in seconds, during which the job run consumed resources.</p>"""
    job_name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The name of the job being processed during this run.</p>"""
    profile_configuration: NotRequired[
        "aws_sdk_databrew.types.profile_configuration.ProfileConfiguration"
    ]
    """<p>Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.</p>"""
    validation_configurations: NotRequired[
        "aws_sdk_databrew.types.validation_configuration_list.ValidationConfigurationList"
    ]
    """<p>List of validation configurations that are applied to the profile job.</p>"""
    run_id: NotRequired["aws_sdk_databrew.types.job_run_id.JobRunId"]
    """<p>The unique identifier of the job run.</p>"""
    state: NotRequired["aws_sdk_databrew.types.job_run_state.JobRunState"]
    """<p>The current state of the job run entity itself.</p>"""
    log_subscription: NotRequired[
        "aws_sdk_databrew.types.log_subscription.LogSubscription"
    ]
    """<p>The current status of Amazon CloudWatch logging for the job run.</p>"""
    log_group_name: NotRequired["aws_sdk_databrew.types.log_group_name.LogGroupName"]
    """<p>The name of an Amazon CloudWatch log group, where the job writes diagnostic messages when it runs.</p>"""
    outputs: NotRequired["aws_sdk_databrew.types.output_list.OutputList"]
    """<p>One or more output artifacts from a job run.</p>"""
    data_catalog_outputs: NotRequired[
        "aws_sdk_databrew.types.data_catalog_output_list.DataCatalogOutputList"
    ]
    """<p>One or more artifacts that represent the Glue Data Catalog output from running the job.</p>"""
    database_outputs: NotRequired[
        "aws_sdk_databrew.types.database_output_list.DatabaseOutputList"
    ]
    """<p>Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.</p>"""
    recipe_reference: NotRequired[
        "aws_sdk_databrew.types.recipe_reference.RecipeReference"
    ]
    started_by: NotRequired["aws_sdk_databrew.types.started_by.StartedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who started the job run.</p>"""
    started_on: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time when the job run began.</p>"""
    job_sample: NotRequired["aws_sdk_databrew.types.job_sample.JobSample"]
    """<p>Sample configuration for profile jobs only. Determines the number of rows on which the profile job will be executed. If a JobSample value is not provided, the default value will be used. The default value is CUSTOM_ROWS for the mode parameter and 20000 for the size parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRunResponse) -> dict:
    out: dict = {}
    out["Attempt"] = value.get("attempt", 0)
    if "completed_on" in value:
        import aws_sdk_databrew.types.date

        out["CompletedOn"] = aws_sdk_databrew.types.date.serialize_json(
            value["completed_on"]
        )
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    out["ExecutionTime"] = value.get("execution_time", 0)
    out["JobName"] = value["job_name"]
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
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "state" in value:
        import aws_sdk_databrew.types.job_run_state

        out["State"] = aws_sdk_databrew.types.job_run_state.serialize_json(
            value["state"]
        )
    if "log_subscription" in value:
        import aws_sdk_databrew.types.log_subscription

        out["LogSubscription"] = aws_sdk_databrew.types.log_subscription.serialize_json(
            value["log_subscription"]
        )
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
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
    if "recipe_reference" in value:
        import aws_sdk_databrew.types.recipe_reference

        out["RecipeReference"] = aws_sdk_databrew.types.recipe_reference.serialize_json(
            value["recipe_reference"]
        )
    if "started_by" in value:
        out["StartedBy"] = value["started_by"]
    if "started_on" in value:
        import aws_sdk_databrew.types.date

        out["StartedOn"] = aws_sdk_databrew.types.date.serialize_json(
            value["started_on"]
        )
    if "job_sample" in value:
        import aws_sdk_databrew.types.job_sample

        out["JobSample"] = aws_sdk_databrew.types.job_sample.serialize_json(
            value["job_sample"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobRunResponse:
    out: DescribeJobRunResponse = {}  # type: ignore[typeddict-item]
    if "Attempt" in data:
        out["attempt"] = data["Attempt"]
    else:
        out["attempt"] = 0
    if "CompletedOn" in data:
        import aws_sdk_databrew.types.date

        out["completed_on"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CompletedOn"]
        )
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ExecutionTime" in data:
        out["execution_time"] = data["ExecutionTime"]
    else:
        out["execution_time"] = 0
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("DescribeJobRunResponse.job_name required")
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
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "State" in data:
        import aws_sdk_databrew.types.job_run_state

        out["state"] = aws_sdk_databrew.types.job_run_state.deserialize_json(
            data["State"]
        )
    if "LogSubscription" in data:
        import aws_sdk_databrew.types.log_subscription

        out["log_subscription"] = (
            aws_sdk_databrew.types.log_subscription.deserialize_json(
                data["LogSubscription"]
            )
        )
    if "LogGroupName" in data:
        out["log_group_name"] = data["LogGroupName"]
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
    if "RecipeReference" in data:
        import aws_sdk_databrew.types.recipe_reference

        out["recipe_reference"] = (
            aws_sdk_databrew.types.recipe_reference.deserialize_json(
                data["RecipeReference"]
            )
        )
    if "StartedBy" in data:
        out["started_by"] = data["StartedBy"]
    if "StartedOn" in data:
        import aws_sdk_databrew.types.date

        out["started_on"] = aws_sdk_databrew.types.date.deserialize_json(
            data["StartedOn"]
        )
    if "JobSample" in data:
        import aws_sdk_databrew.types.job_sample

        out["job_sample"] = aws_sdk_databrew.types.job_sample.deserialize_json(
            data["JobSample"]
        )
    return out

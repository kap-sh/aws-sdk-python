"""Generated from Smithy shape ``com.amazonaws.personalize#CreateBatchInferenceJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.batch_inference_job_config
    import aws_sdk_personalize.types.batch_inference_job_input
    import aws_sdk_personalize.types.batch_inference_job_mode
    import aws_sdk_personalize.types.batch_inference_job_output
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.num_batch_results
    import aws_sdk_personalize.types.role_arn
    import aws_sdk_personalize.types.tags
    import aws_sdk_personalize.types.theme_generation_config


class CreateBatchInferenceJobRequest(TypedDict):
    job_name: "aws_sdk_personalize.types.name.Name"
    """<p>The name of the batch inference job to create.</p>"""
    solution_version_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution version that will be used to generate the batch inference recommendations.</p>"""
    filter_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    r"""<p>The ARN of the filter to apply to the batch inference job. For more information on using filters, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/filter-batch.html\">Filtering batch recommendations</a>.</p>"""
    num_results: NotRequired[
        "aws_sdk_personalize.types.num_batch_results.NumBatchResults"
    ]
    """<p>The number of recommendations to retrieve.</p>"""
    job_input: (
        "aws_sdk_personalize.types.batch_inference_job_input.BatchInferenceJobInput"
    )
    """<p>The Amazon S3 path that leads to the input file to base your recommendations on. The input material must be in JSON format.</p>"""
    job_output: (
        "aws_sdk_personalize.types.batch_inference_job_output.BatchInferenceJobOutput"
    )
    """<p>The path to the Amazon S3 bucket where the job's output will be stored.</p>"""
    role_arn: "aws_sdk_personalize.types.role_arn.RoleArn"
    """<p>The ARN of the Amazon Identity and Access Management role that has permissions to read and write to your input and output Amazon S3 buckets respectively.</p>"""
    batch_inference_job_config: NotRequired[
        "aws_sdk_personalize.types.batch_inference_job_config.BatchInferenceJobConfig"
    ]
    """<p>The configuration details of a batch inference job.</p>"""
    tags: NotRequired["aws_sdk_personalize.types.tags.Tags"]
    r"""<p>A list of <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html\">tags</a> to apply to the batch inference job.</p>"""
    batch_inference_job_mode: NotRequired[
        "aws_sdk_personalize.types.batch_inference_job_mode.BatchInferenceJobMode"
    ]
    r"""<p>The mode of the batch inference job. To generate descriptive themes for groups of similar items, set the job mode to <code>THEME_GENERATION</code>. If you don't want to generate themes, use the default <code>BATCH_INFERENCE</code>.</p> <p> When you get batch recommendations with themes, you will incur additional costs. For more information, see <a href=\"https://aws.amazon.com/personalize/pricing/\">Amazon Personalize pricing</a>. </p>"""
    theme_generation_config: NotRequired[
        "aws_sdk_personalize.types.theme_generation_config.ThemeGenerationConfig"
    ]
    """<p>For theme generation jobs, specify the name of the column in your Items dataset that contains each item's name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchInferenceJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["solutionVersionArn"] = value["solution_version_arn"]
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    if "num_results" in value:
        out["numResults"] = value["num_results"]
    import aws_sdk_personalize.types.batch_inference_job_input

    out["jobInput"] = (
        aws_sdk_personalize.types.batch_inference_job_input.serialize_aws_json_1_1(
            value["job_input"]
        )
    )
    import aws_sdk_personalize.types.batch_inference_job_output

    out["jobOutput"] = (
        aws_sdk_personalize.types.batch_inference_job_output.serialize_aws_json_1_1(
            value["job_output"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "batch_inference_job_config" in value:
        import aws_sdk_personalize.types.batch_inference_job_config

        out["batchInferenceJobConfig"] = (
            aws_sdk_personalize.types.batch_inference_job_config.serialize_aws_json_1_1(
                value["batch_inference_job_config"]
            )
        )
    if "tags" in value:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "batch_inference_job_mode" in value:
        import aws_sdk_personalize.types.batch_inference_job_mode

        out["batchInferenceJobMode"] = (
            aws_sdk_personalize.types.batch_inference_job_mode.serialize_aws_json_1_1(
                value["batch_inference_job_mode"]
            )
        )
    if "theme_generation_config" in value:
        import aws_sdk_personalize.types.theme_generation_config

        out["themeGenerationConfig"] = (
            aws_sdk_personalize.types.theme_generation_config.serialize_aws_json_1_1(
                value["theme_generation_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchInferenceJobRequest:
    out: CreateBatchInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.job_name required")
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    else:
        raise DeserializationError(
            "CreateBatchInferenceJobRequest.solution_version_arn required"
        )
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    if "numResults" in data:
        out["num_results"] = data["numResults"]
    if "jobInput" in data:
        import aws_sdk_personalize.types.batch_inference_job_input

        out["job_input"] = (
            aws_sdk_personalize.types.batch_inference_job_input.deserialize_aws_json_1_1(
                data["jobInput"]
            )
        )
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.job_input required")
    if "jobOutput" in data:
        import aws_sdk_personalize.types.batch_inference_job_output

        out["job_output"] = (
            aws_sdk_personalize.types.batch_inference_job_output.deserialize_aws_json_1_1(
                data["jobOutput"]
            )
        )
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.job_output required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateBatchInferenceJobRequest.role_arn required")
    if "batchInferenceJobConfig" in data:
        import aws_sdk_personalize.types.batch_inference_job_config

        out["batch_inference_job_config"] = (
            aws_sdk_personalize.types.batch_inference_job_config.deserialize_aws_json_1_1(
                data["batchInferenceJobConfig"]
            )
        )
    if "tags" in data:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "batchInferenceJobMode" in data:
        import aws_sdk_personalize.types.batch_inference_job_mode

        out["batch_inference_job_mode"] = (
            aws_sdk_personalize.types.batch_inference_job_mode.deserialize_aws_json_1_1(
                data["batchInferenceJobMode"]
            )
        )
    if "themeGenerationConfig" in data:
        import aws_sdk_personalize.types.theme_generation_config

        out["theme_generation_config"] = (
            aws_sdk_personalize.types.theme_generation_config.deserialize_aws_json_1_1(
                data["themeGenerationConfig"]
            )
        )
    return out

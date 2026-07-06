"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanLoopConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.flow_definition_task_availability_lifetime_in_seconds
    import aws_sdk_sagemaker.types.flow_definition_task_count
    import aws_sdk_sagemaker.types.flow_definition_task_description
    import aws_sdk_sagemaker.types.flow_definition_task_keywords
    import aws_sdk_sagemaker.types.flow_definition_task_time_limit_in_seconds
    import aws_sdk_sagemaker.types.flow_definition_task_title
    import aws_sdk_sagemaker.types.human_task_ui_arn
    import aws_sdk_sagemaker.types.public_workforce_task_price
    import aws_sdk_sagemaker.types.workteam_arn


class HumanLoopConfig(TypedDict, closed=True):
    workteam_arn: NotRequired["aws_sdk_sagemaker.types.workteam_arn.WorkteamArn"]
    r"""<p>Amazon Resource Name (ARN) of a team of workers. To learn more about the types of workforces and work teams you can create and use with Amazon A2I, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html\">Create and Manage Workforces</a>.</p>"""
    human_task_ui_arn: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_arn.HumanTaskUiArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the human task user interface.</p> <p>You can use standard HTML and Crowd HTML Elements to create a custom worker task template. You use this template to create a human task UI.</p> <p>To learn how to create a custom HTML template, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-custom-templates.html\">Create Custom Worker Task Template</a>.</p> <p>To learn how to create a human task UI, which is a worker task template that can be used in a flow definition, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-worker-template-console.html\">Create and Delete a Worker Task Templates</a>.</p>"""
    task_title: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_task_title.FlowDefinitionTaskTitle"
    ]
    """<p>A title for the human worker task.</p>"""
    task_description: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_task_description.FlowDefinitionTaskDescription"
    ]
    """<p>A description for the human worker task.</p>"""
    task_count: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_task_count.FlowDefinitionTaskCount"
    ]
    """<p>The number of distinct workers who will perform the same task on each object. For example, if <code>TaskCount</code> is set to <code>3</code> for an image classification labeling job, three workers will classify each input image. Increasing <code>TaskCount</code> can improve label accuracy.</p>"""
    task_availability_lifetime_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_task_availability_lifetime_in_seconds.FlowDefinitionTaskAvailabilityLifetimeInSeconds"
    ]
    """<p>The length of time that a task remains available for review by human workers.</p>"""
    task_time_limit_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_task_time_limit_in_seconds.FlowDefinitionTaskTimeLimitInSeconds"
    ]
    """<p>The amount of time that a worker has to complete a task. The default value is 3,600 seconds (1 hour).</p>"""
    task_keywords: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_task_keywords.FlowDefinitionTaskKeywords"
    ]
    """<p>Keywords used to describe the task so that workers can discover the task.</p>"""
    public_workforce_task_price: NotRequired[
        "aws_sdk_sagemaker.types.public_workforce_task_price.PublicWorkforceTaskPrice"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopConfig) -> dict:
    out: dict = {}
    if "workteam_arn" in value:
        out["WorkteamArn"] = value["workteam_arn"]
    if "human_task_ui_arn" in value:
        out["HumanTaskUiArn"] = value["human_task_ui_arn"]
    if "task_title" in value:
        out["TaskTitle"] = value["task_title"]
    if "task_description" in value:
        out["TaskDescription"] = value["task_description"]
    if "task_count" in value:
        out["TaskCount"] = value["task_count"]
    if "task_availability_lifetime_in_seconds" in value:
        out["TaskAvailabilityLifetimeInSeconds"] = value[
            "task_availability_lifetime_in_seconds"
        ]
    if "task_time_limit_in_seconds" in value:
        out["TaskTimeLimitInSeconds"] = value["task_time_limit_in_seconds"]
    if "task_keywords" in value:
        import aws_sdk_sagemaker.types.flow_definition_task_keywords

        out["TaskKeywords"] = (
            aws_sdk_sagemaker.types.flow_definition_task_keywords.serialize_aws_json_1_1(
                value["task_keywords"]
            )
        )
    if "public_workforce_task_price" in value:
        import aws_sdk_sagemaker.types.public_workforce_task_price

        out["PublicWorkforceTaskPrice"] = (
            aws_sdk_sagemaker.types.public_workforce_task_price.serialize_aws_json_1_1(
                value["public_workforce_task_price"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopConfig:
    out: HumanLoopConfig = {}  # type: ignore[typeddict-item]
    if "WorkteamArn" in data:
        out["workteam_arn"] = data["WorkteamArn"]
    if "HumanTaskUiArn" in data:
        out["human_task_ui_arn"] = data["HumanTaskUiArn"]
    if "TaskTitle" in data:
        out["task_title"] = data["TaskTitle"]
    if "TaskDescription" in data:
        out["task_description"] = data["TaskDescription"]
    if "TaskCount" in data:
        out["task_count"] = data["TaskCount"]
    if "TaskAvailabilityLifetimeInSeconds" in data:
        out["task_availability_lifetime_in_seconds"] = data[
            "TaskAvailabilityLifetimeInSeconds"
        ]
    if "TaskTimeLimitInSeconds" in data:
        out["task_time_limit_in_seconds"] = data["TaskTimeLimitInSeconds"]
    if "TaskKeywords" in data:
        import aws_sdk_sagemaker.types.flow_definition_task_keywords

        out["task_keywords"] = (
            aws_sdk_sagemaker.types.flow_definition_task_keywords.deserialize_aws_json_1_1(
                data["TaskKeywords"]
            )
        )
    if "PublicWorkforceTaskPrice" in data:
        import aws_sdk_sagemaker.types.public_workforce_task_price

        out["public_workforce_task_price"] = (
            aws_sdk_sagemaker.types.public_workforce_task_price.deserialize_aws_json_1_1(
                data["PublicWorkforceTaskPrice"]
            )
        )
    return out

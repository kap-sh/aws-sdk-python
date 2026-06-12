"""Generated from Smithy shape ``com.amazonaws.snowball#LambdaResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.event_trigger_definition_list
    import aws_sdk_snowball.types.resource_arn


class LambdaResource(TypedDict):
    lambda_arn: NotRequired["aws_sdk_snowball.types.resource_arn.ResourceARN"]
    """<p>An Amazon Resource Name (ARN) that represents an Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.</p>"""
    event_triggers: NotRequired[
        "aws_sdk_snowball.types.event_trigger_definition_list.EventTriggerDefinitionList"
    ]
    """<p>The array of ARNs for <a>S3Resource</a> objects to trigger the <a>LambdaResource</a> objects associated with this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaResource) -> dict:
    out: dict = {}
    if "lambda_arn" in value:
        out["LambdaArn"] = value["lambda_arn"]
    if "event_triggers" in value:
        import aws_sdk_snowball.types.event_trigger_definition_list

        out["EventTriggers"] = (
            aws_sdk_snowball.types.event_trigger_definition_list.serialize_aws_json_1_1(
                value["event_triggers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaResource:
    out: LambdaResource = {}  # type: ignore[typeddict-item]
    if "LambdaArn" in data:
        out["lambda_arn"] = data["LambdaArn"]
    if "EventTriggers" in data:
        import aws_sdk_snowball.types.event_trigger_definition_list

        out["event_triggers"] = (
            aws_sdk_snowball.types.event_trigger_definition_list.deserialize_aws_json_1_1(
                data["EventTriggers"]
            )
        )
    return out

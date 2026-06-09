"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionEventInvokeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.date
    import aws_sdk_lambda.types.destination_config
    import aws_sdk_lambda.types.function_arn
    import aws_sdk_lambda.types.maximum_event_age_in_seconds
    import aws_sdk_lambda.types.maximum_retry_attempts


class FunctionEventInvokeConfig(TypedDict):
    last_modified: NotRequired["aws_sdk_lambda.types.date.Date"]
    """<p>The date and time that the configuration was last updated.</p>"""
    function_arn: NotRequired["aws_sdk_lambda.types.function_arn.FunctionArn"]
    """<p>The Amazon Resource Name (ARN) of the function.</p>"""
    maximum_retry_attempts: NotRequired[
        "aws_sdk_lambda.types.maximum_retry_attempts.MaximumRetryAttempts"
    ]
    """<p>The maximum number of times to retry when the function returns an error.</p>"""
    maximum_event_age_in_seconds: NotRequired[
        "aws_sdk_lambda.types.maximum_event_age_in_seconds.MaximumEventAgeInSeconds"
    ]
    """<p>The maximum age of a request that Lambda sends to a function for processing.</p>"""
    destination_config: NotRequired[
        "aws_sdk_lambda.types.destination_config.DestinationConfig"
    ]
    """<p>A destination for events after they have been sent to a function for processing.</p> <p class=\"title\"> <b>Destinations</b> </p> <ul> <li> <p> <b>Function</b> - The Amazon Resource Name (ARN) of a Lambda function.</p> </li> <li> <p> <b>Queue</b> - The ARN of a standard SQS queue.</p> </li> <li> <p> <b>Bucket</b> - The ARN of an Amazon S3 bucket.</p> </li> <li> <p> <b>Topic</b> - The ARN of a standard SNS topic.</p> </li> <li> <p> <b>Event Bus</b> - The ARN of an Amazon EventBridge event bus.</p> </li> </ul> <note> <p>S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionEventInvokeConfig) -> dict:
    out: dict = {}
    if "last_modified" in value:
        import aws_sdk_lambda.types.date

        out["LastModified"] = aws_sdk_lambda.types.date.serialize_json(
            value["last_modified"]
        )
    if "function_arn" in value:
        out["FunctionArn"] = value["function_arn"]
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    if "maximum_event_age_in_seconds" in value:
        out["MaximumEventAgeInSeconds"] = value["maximum_event_age_in_seconds"]
    if "destination_config" in value:
        import aws_sdk_lambda.types.destination_config

        out["DestinationConfig"] = (
            aws_sdk_lambda.types.destination_config.serialize_json(
                value["destination_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunctionEventInvokeConfig:
    out: FunctionEventInvokeConfig = {}  # type: ignore[typeddict-item]
    if "LastModified" in data:
        import aws_sdk_lambda.types.date

        out["last_modified"] = aws_sdk_lambda.types.date.deserialize_json(
            data["LastModified"]
        )
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    if "MaximumRetryAttempts" in data:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    if "MaximumEventAgeInSeconds" in data:
        out["maximum_event_age_in_seconds"] = data["MaximumEventAgeInSeconds"]
    if "DestinationConfig" in data:
        import aws_sdk_lambda.types.destination_config

        out["destination_config"] = (
            aws_sdk_lambda.types.destination_config.deserialize_json(
                data["DestinationConfig"]
            )
        )
    return out

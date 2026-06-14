"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#LambdaOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class LambdaOutput(TypedDict):
    resource_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    r"""<p>The Amazon Resource Name (ARN) of the destination Lambda function to write to.</p> <note> <p>To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda\">Example ARNs: Amazon Lambda</a> </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaOutput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaOutput:
    out: LambdaOutput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("LambdaOutput.resource_arn required")
    return out

"""Generated from Smithy shape ``com.amazonaws.sfn#RedriveExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.client_token


class RedriveExecutionInput(TypedDict):
    execution_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the execution to be redriven.</p>"""
    client_token: NotRequired["aws_sdk_sfn.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The API will return idempotent responses for the last 10 client tokens used to successfully redrive the execution. These client tokens are valid for up to 15 minutes after they are first used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RedriveExecutionInput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RedriveExecutionInput:
    out: RedriveExecutionInput = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("RedriveExecutionInput.execution_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

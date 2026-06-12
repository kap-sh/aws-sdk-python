"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.included_data


class DescribeExecutionInput(TypedDict):
    execution_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the execution to describe.</p>"""
    included_data: NotRequired["aws_sdk_sfn.types.included_data.IncludedData"]
    """<p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call DescribeStateMachine API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeExecutionInput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    if "included_data" in value:
        import aws_sdk_sfn.types.included_data

        out["includedData"] = aws_sdk_sfn.types.included_data.serialize_aws_json_1_0(
            value["included_data"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeExecutionInput:
    out: DescribeExecutionInput = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("DescribeExecutionInput.execution_arn required")
    if "includedData" in data:
        import aws_sdk_sfn.types.included_data

        out["included_data"] = aws_sdk_sfn.types.included_data.deserialize_aws_json_1_0(
            data["includedData"]
        )
    return out

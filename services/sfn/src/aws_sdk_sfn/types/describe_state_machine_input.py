"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeStateMachineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.included_data


class DescribeStateMachineInput(TypedDict, closed=True):
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine for which you want the information.</p> <p>If you specify a state machine version ARN, this API returns details about that version. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, <code>stateMachineARN:1</code>.</p>"""
    included_data: NotRequired["aws_sdk_sfn.types.included_data.IncludedData"]
    """<p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call the API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p> <note> <p> When calling a labelled ARN for an encrypted state machine, the <code>includedData = METADATA_ONLY</code> parameter will not apply because Step Functions needs to decrypt the entire state machine definition to get the Distributed Map state’s definition. In this case, the API caller needs to have <code>kms:Decrypt</code> permission. </p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStateMachineInput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    if "included_data" in value:
        import aws_sdk_sfn.types.included_data

        out["includedData"] = aws_sdk_sfn.types.included_data.serialize_aws_json_1_0(
            value["included_data"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStateMachineInput:
    out: DescribeStateMachineInput = {}  # type: ignore[typeddict-item]
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError(
            "DescribeStateMachineInput.state_machine_arn required"
        )
    if "includedData" in data:
        import aws_sdk_sfn.types.included_data

        out["included_data"] = aws_sdk_sfn.types.included_data.deserialize_aws_json_1_0(
            data["includedData"]
        )
    return out

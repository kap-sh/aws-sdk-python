"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeImportInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_arn


class DescribeImportInput(TypedDict):
    import_arn: "aws_sdk_dynamodb.types.import_arn.ImportArn"
    """<p> The Amazon Resource Name (ARN) associated with the table you're importing to. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeImportInput) -> dict:
    out: dict = {}
    out["ImportArn"] = value["import_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeImportInput:
    out: DescribeImportInput = {}  # type: ignore[typeddict-item]
    if "ImportArn" in data:
        out["import_arn"] = data["ImportArn"]
    else:
        raise DeserializationError("DescribeImportInput.import_arn required")
    return out

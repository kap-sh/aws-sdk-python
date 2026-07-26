"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeExportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.export_arn


class DescribeExportInput(TypedDict, closed=True):
    export_arn: "capo_dynamodb.types.export_arn.ExportArn"
    """<p>The Amazon Resource Name (ARN) associated with the export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeExportInput) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeExportInput:
    out: DescribeExportInput = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    else:
        raise DeserializationError("DescribeExportInput.export_arn required")
    return out

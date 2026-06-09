"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeExportOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_description


class DescribeExportOutput(TypedDict):
    export_description: NotRequired[
        "aws_sdk_dynamodb.types.export_description.ExportDescription"
    ]
    """<p>Represents the properties of the export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeExportOutput) -> dict:
    out: dict = {}
    if "export_description" in value:
        import aws_sdk_dynamodb.types.export_description

        out["ExportDescription"] = (
            aws_sdk_dynamodb.types.export_description.serialize_aws_json_1_0(
                value["export_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeExportOutput:
    out: DescribeExportOutput = {}  # type: ignore[typeddict-item]
    if "ExportDescription" in data:
        import aws_sdk_dynamodb.types.export_description

        out["export_description"] = (
            aws_sdk_dynamodb.types.export_description.deserialize_aws_json_1_0(
                data["ExportDescription"]
            )
        )
    return out

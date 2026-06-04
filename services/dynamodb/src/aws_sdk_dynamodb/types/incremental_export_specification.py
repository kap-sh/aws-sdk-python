"""Generated from Smithy shape ``com.amazonaws.dynamodb#IncrementalExportSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_from_time
    import aws_sdk_dynamodb.types.export_to_time
    import aws_sdk_dynamodb.types.export_view_type


class IncrementalExportSpecification(TypedDict):
    export_from_time: NotRequired[
        "aws_sdk_dynamodb.types.export_from_time.ExportFromTime"
    ]
    """<p>Time in the past which provides the inclusive start range for the export table's data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the table's state including and after this point in time.</p>"""
    export_to_time: NotRequired["aws_sdk_dynamodb.types.export_to_time.ExportToTime"]
    """<p>Time in the past which provides the exclusive end range for the export table's data, counted in seconds from the start of the Unix epoch. The incremental export will reflect the table's state just prior to this point in time. If this is not provided, the latest time with data available will be used.</p>"""
    export_view_type: NotRequired[
        "aws_sdk_dynamodb.types.export_view_type.ExportViewType"
    ]
    """<p>The view type that was chosen for the export. Valid values are <code>NEW_AND_OLD_IMAGES</code> and <code>NEW_IMAGES</code>. The default value is <code>NEW_AND_OLD_IMAGES</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IncrementalExportSpecification) -> dict:
    out: dict = {}
    if "export_from_time" in value:
        import aws_sdk_dynamodb.types.export_from_time

        out["ExportFromTime"] = (
            aws_sdk_dynamodb.types.export_from_time.serialize_aws_json_1_0(
                value["export_from_time"]
            )
        )
    if "export_to_time" in value:
        import aws_sdk_dynamodb.types.export_to_time

        out["ExportToTime"] = (
            aws_sdk_dynamodb.types.export_to_time.serialize_aws_json_1_0(
                value["export_to_time"]
            )
        )
    if "export_view_type" in value:
        import aws_sdk_dynamodb.types.export_view_type

        out["ExportViewType"] = (
            aws_sdk_dynamodb.types.export_view_type.serialize_aws_json_1_0(
                value["export_view_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IncrementalExportSpecification:
    out: IncrementalExportSpecification = {}  # type: ignore[typeddict-item]
    if "ExportFromTime" in data:
        import aws_sdk_dynamodb.types.export_from_time

        out["export_from_time"] = (
            aws_sdk_dynamodb.types.export_from_time.deserialize_aws_json_1_0(
                data["ExportFromTime"]
            )
        )
    if "ExportToTime" in data:
        import aws_sdk_dynamodb.types.export_to_time

        out["export_to_time"] = (
            aws_sdk_dynamodb.types.export_to_time.deserialize_aws_json_1_0(
                data["ExportToTime"]
            )
        )
    if "ExportViewType" in data:
        import aws_sdk_dynamodb.types.export_view_type

        out["export_view_type"] = (
            aws_sdk_dynamodb.types.export_view_type.deserialize_aws_json_1_0(
                data["ExportViewType"]
            )
        )
    return out

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

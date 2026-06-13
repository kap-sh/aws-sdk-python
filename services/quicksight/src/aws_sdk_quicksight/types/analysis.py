"""Generated from Smithy shape ``com.amazonaws.quicksight#Analysis``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_error_list
    import aws_sdk_quicksight.types.analysis_name
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_set_arns_list
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.sheet_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.timestamp


class Analysis(TypedDict):
    analysis_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the analysis.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.analysis_name.AnalysisName"]
    """<p>The descriptive name of the analysis.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.resource_status.ResourceStatus"]
    """<p>Status associated with the analysis.</p>"""
    errors: NotRequired[
        "aws_sdk_quicksight.types.analysis_error_list.AnalysisErrorList"
    ]
    """<p>Errors associated with the analysis.</p>"""
    data_set_arns: NotRequired[
        "aws_sdk_quicksight.types.data_set_arns_list.DataSetArnsList"
    ]
    """<p>The ARNs of the datasets of the analysis.</p>"""
    theme_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme of the analysis.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the analysis was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the analysis was last updated.</p>"""
    sheets: NotRequired["aws_sdk_quicksight.types.sheet_list.SheetList"]
    """<p>A list of the associated sheets with the unique identifier and name of each sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Analysis) -> dict:
    out: dict = {}
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["Status"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "errors" in value:
        import aws_sdk_quicksight.types.analysis_error_list

        out["Errors"] = aws_sdk_quicksight.types.analysis_error_list.serialize_json(
            value["errors"]
        )
    if "data_set_arns" in value:
        import aws_sdk_quicksight.types.data_set_arns_list

        out["DataSetArns"] = aws_sdk_quicksight.types.data_set_arns_list.serialize_json(
            value["data_set_arns"]
        )
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "sheets" in value:
        import aws_sdk_quicksight.types.sheet_list

        out["Sheets"] = aws_sdk_quicksight.types.sheet_list.serialize_json(
            value["sheets"]
        )
    return out


def deserialize_json(data: dict) -> Analysis:
    out: Analysis = {}  # type: ignore[typeddict-item]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_quicksight.types.resource_status

        out["status"] = aws_sdk_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "Errors" in data:
        import aws_sdk_quicksight.types.analysis_error_list

        out["errors"] = aws_sdk_quicksight.types.analysis_error_list.deserialize_json(
            data["Errors"]
        )
    if "DataSetArns" in data:
        import aws_sdk_quicksight.types.data_set_arns_list

        out["data_set_arns"] = (
            aws_sdk_quicksight.types.data_set_arns_list.deserialize_json(
                data["DataSetArns"]
            )
        )
    if "ThemeArn" in data:
        out["theme_arn"] = data["ThemeArn"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "Sheets" in data:
        import aws_sdk_quicksight.types.sheet_list

        out["sheets"] = aws_sdk_quicksight.types.sheet_list.deserialize_json(
            data["Sheets"]
        )
    return out

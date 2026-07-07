"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAnalysisDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_definition
    import aws_sdk_quicksight.types.analysis_error_list
    import aws_sdk_quicksight.types.analysis_name
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeAnalysisDefinitionResponse(TypedDict, closed=True):
    analysis_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis described.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.analysis_name.AnalysisName"]
    """<p>The descriptive name of the analysis.</p>"""
    errors: NotRequired[
        "aws_sdk_quicksight.types.analysis_error_list.AnalysisErrorList"
    ]
    """<p>Errors associated with the analysis.</p>"""
    resource_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>Status associated with the analysis.</p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATION_SUCCESSFUL</code> </p> </li> <li> <p> <code>CREATION_FAILED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> </p> </li> <li> <p> <code>UPDATE_FAILED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
    theme_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme of the analysis.</p>"""
    definition: NotRequired[
        "aws_sdk_quicksight.types.analysis_definition.AnalysisDefinition"
    ]
    """<p>The definition of an analysis.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnalysisDefinitionResponse) -> dict:
    out: dict = {}
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "errors" in value:
        import aws_sdk_quicksight.types.analysis_error_list

        out["Errors"] = aws_sdk_quicksight.types.analysis_error_list.serialize_json(
            value["errors"]
        )
    if "resource_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["ResourceStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["resource_status"]
        )
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "definition" in value:
        import aws_sdk_quicksight.types.analysis_definition

        out["Definition"] = aws_sdk_quicksight.types.analysis_definition.serialize_json(
            value["definition"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAnalysisDefinitionResponse:
    out: DescribeAnalysisDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Errors" in data:
        import aws_sdk_quicksight.types.analysis_error_list

        out["errors"] = aws_sdk_quicksight.types.analysis_error_list.deserialize_json(
            data["Errors"]
        )
    if "ResourceStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["resource_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["ResourceStatus"]
            )
        )
    if "ThemeArn" in data:
        out["theme_arn"] = data["ThemeArn"]
    if "Definition" in data:
        import aws_sdk_quicksight.types.analysis_definition

        out["definition"] = (
            aws_sdk_quicksight.types.analysis_definition.deserialize_json(
                data["Definition"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

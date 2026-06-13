"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAnalysisResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class CreateAnalysisResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN for the analysis.</p>"""
    analysis_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis.</p>"""
    creation_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The status of the creation of the analysis. </p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalysisResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "creation_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["CreationStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["creation_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateAnalysisResponse:
    out: CreateAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "CreationStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["creation_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

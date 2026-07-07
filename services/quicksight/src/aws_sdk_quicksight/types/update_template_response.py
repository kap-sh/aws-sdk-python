"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateTemplateResponse(TypedDict, closed=True):
    template_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the template.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the template.</p>"""
    version_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN for the template, including the version information of the first version.</p>"""
    creation_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The creation status of the template.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateResponse) -> dict:
    out: dict = {}
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "version_arn" in value:
        out["VersionArn"] = value["version_arn"]
    if "creation_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["CreationStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["creation_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateTemplateResponse:
    out: UpdateTemplateResponse = {}  # type: ignore[typeddict-item]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VersionArn" in data:
        out["version_arn"] = data["VersionArn"]
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

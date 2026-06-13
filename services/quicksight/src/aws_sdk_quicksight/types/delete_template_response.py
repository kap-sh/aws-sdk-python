"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DeleteTemplateResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    template_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>An ID for the template.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTemplateResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> DeleteTemplateResponse:
    out: DeleteTemplateResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    return out

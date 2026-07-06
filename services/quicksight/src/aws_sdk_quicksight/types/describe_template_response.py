"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.template


class DescribeTemplateResponse(TypedDict, closed=True):
    template: NotRequired["aws_sdk_quicksight.types.template.Template"]
    """<p>The template structure for the object you want to describe.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTemplateResponse) -> dict:
    out: dict = {}
    if "template" in value:
        import aws_sdk_quicksight.types.template

        out["Template"] = aws_sdk_quicksight.types.template.serialize_json(
            value["template"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeTemplateResponse:
    out: DescribeTemplateResponse = {}  # type: ignore[typeddict-item]
    if "Template" in data:
        import aws_sdk_quicksight.types.template

        out["template"] = aws_sdk_quicksight.types.template.deserialize_json(
            data["Template"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

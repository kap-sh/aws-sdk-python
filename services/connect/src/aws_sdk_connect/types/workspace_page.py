"""Generated from Smithy shape ``com.amazonaws.connect#WorkspacePage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.input_data
    import aws_sdk_connect.types.page
    import aws_sdk_connect.types.slug


class WorkspacePage(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view associated with this page.</p>"""
    page: NotRequired["aws_sdk_connect.types.page.Page"]
    """<p>The page identifier. System pages include <code>HOME</code> and <code>AGENT_EXPERIENCE</code>.</p>"""
    slug: NotRequired["aws_sdk_connect.types.slug.Slug"]
    """<p>The URL-friendly identifier for the page.</p>"""
    input_data: NotRequired["aws_sdk_connect.types.input_data.InputData"]
    """<p>A JSON string containing input parameters passed to the view when the page is rendered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspacePage) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "page" in value:
        out["Page"] = value["page"]
    if "slug" in value:
        out["Slug"] = value["slug"]
    if "input_data" in value:
        out["InputData"] = value["input_data"]
    return out


def deserialize_json(data: dict) -> WorkspacePage:
    out: WorkspacePage = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Page" in data:
        out["page"] = data["Page"]
    if "Slug" in data:
        out["slug"] = data["Slug"]
    if "InputData" in data:
        out["input_data"] = data["InputData"]
    return out

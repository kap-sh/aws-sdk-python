"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardLinksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.link_entity_arn_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateDashboardLinksResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    dashboard_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dashboard.</p>"""
    link_entities: NotRequired[
        "aws_sdk_quicksight.types.link_entity_arn_list.LinkEntityArnList"
    ]
    """<p>A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardLinksResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "link_entities" in value:
        import aws_sdk_quicksight.types.link_entity_arn_list

        out["LinkEntities"] = (
            aws_sdk_quicksight.types.link_entity_arn_list.serialize_json(
                value["link_entities"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDashboardLinksResponse:
    out: UpdateDashboardLinksResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "DashboardArn" in data:
        out["dashboard_arn"] = data["DashboardArn"]
    if "LinkEntities" in data:
        import aws_sdk_quicksight.types.link_entity_arn_list

        out["link_entities"] = (
            aws_sdk_quicksight.types.link_entity_arn_list.deserialize_json(
                data["LinkEntities"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateDashboardRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.dashboard_definition
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.tag_map


class CreateDashboardRequest(TypedDict):
    project_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project in which to create the dashboard.</p>"""
    dashboard_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>A friendly name for the dashboard.</p>"""
    dashboard_description: NotRequired[
        "aws_sdk_iotsitewise.types.description.Description"
    ]
    """<p>A description for the dashboard.</p>"""
    dashboard_definition: (
        "aws_sdk_iotsitewise.types.dashboard_definition.DashboardDefinition"
    )
    """<p>The dashboard definition specified in a JSON literal.</p> <ul> <li> <p>IoT SiteWise Monitor (Classic) see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html\">Create dashboards (CLI)</a> </p> </li> <li> <p>IoT SiteWise Monitor (AI-aware) see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html\">Create dashboards (CLI)</a> </p> </li> </ul> <p>in the <i>IoT SiteWise User Guide</i> </p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    tags: NotRequired["aws_sdk_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the dashboard. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDashboardRequest) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    out["dashboardName"] = value["dashboard_name"]
    if "dashboard_description" in value:
        out["dashboardDescription"] = value["dashboard_description"]
    out["dashboardDefinition"] = value["dashboard_definition"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDashboardRequest:
    out: CreateDashboardRequest = {}  # type: ignore[typeddict-item]
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("CreateDashboardRequest.project_id required")
    if "dashboardName" in data:
        out["dashboard_name"] = data["dashboardName"]
    else:
        raise DeserializationError("CreateDashboardRequest.dashboard_name required")
    if "dashboardDescription" in data:
        out["dashboard_description"] = data["dashboardDescription"]
    if "dashboardDefinition" in data:
        out["dashboard_definition"] = data["dashboardDefinition"]
    else:
        raise DeserializationError(
            "CreateDashboardRequest.dashboard_definition required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out

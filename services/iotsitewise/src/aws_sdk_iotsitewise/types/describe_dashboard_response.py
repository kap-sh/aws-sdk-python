"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.dashboard_definition
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.timestamp


class DescribeDashboardResponse(TypedDict, closed=True):
    dashboard_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the dashboard.</p>"""
    dashboard_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the dashboard, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}</code> </p>"""
    dashboard_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the dashboard.</p>"""
    project_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project that the dashboard is in.</p>"""
    dashboard_description: NotRequired[
        "aws_sdk_iotsitewise.types.description.Description"
    ]
    """<p>The dashboard's description.</p>"""
    dashboard_definition: (
        "aws_sdk_iotsitewise.types.dashboard_definition.DashboardDefinition"
    )
    r"""<p>The dashboard's definition JSON literal. For detailed information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html\">Creating dashboards (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    dashboard_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dashboard was created, in Unix epoch time.</p>"""
    dashboard_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dashboard was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardResponse) -> dict:
    out: dict = {}
    out["dashboardId"] = value["dashboard_id"]
    out["dashboardArn"] = value["dashboard_arn"]
    out["dashboardName"] = value["dashboard_name"]
    out["projectId"] = value["project_id"]
    if "dashboard_description" in value:
        out["dashboardDescription"] = value["dashboard_description"]
    out["dashboardDefinition"] = value["dashboard_definition"]
    import aws_sdk_iotsitewise.types.timestamp

    out["dashboardCreationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["dashboard_creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["dashboardLastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["dashboard_last_update_date"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDashboardResponse:
    out: DescribeDashboardResponse = {}  # type: ignore[typeddict-item]
    if "dashboardId" in data:
        out["dashboard_id"] = data["dashboardId"]
    else:
        raise DeserializationError("DescribeDashboardResponse.dashboard_id required")
    if "dashboardArn" in data:
        out["dashboard_arn"] = data["dashboardArn"]
    else:
        raise DeserializationError("DescribeDashboardResponse.dashboard_arn required")
    if "dashboardName" in data:
        out["dashboard_name"] = data["dashboardName"]
    else:
        raise DeserializationError("DescribeDashboardResponse.dashboard_name required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DescribeDashboardResponse.project_id required")
    if "dashboardDescription" in data:
        out["dashboard_description"] = data["dashboardDescription"]
    if "dashboardDefinition" in data:
        out["dashboard_definition"] = data["dashboardDefinition"]
    else:
        raise DeserializationError(
            "DescribeDashboardResponse.dashboard_definition required"
        )
    if "dashboardCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["dashboard_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["dashboardCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDashboardResponse.dashboard_creation_date required"
        )
    if "dashboardLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["dashboard_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["dashboardLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDashboardResponse.dashboard_last_update_date required"
        )
    return out

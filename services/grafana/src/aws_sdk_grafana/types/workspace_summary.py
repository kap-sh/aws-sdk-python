"""Generated from Smithy shape ``com.amazonaws.grafana#WorkspaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_grafana.types.authentication_summary
    import aws_sdk_grafana.types.description
    import aws_sdk_grafana.types.endpoint
    import aws_sdk_grafana.types.grafana_token
    import aws_sdk_grafana.types.grafana_version
    import aws_sdk_grafana.types.license_type
    import aws_sdk_grafana.types.notification_destinations_list
    import aws_sdk_grafana.types.tag_map
    import aws_sdk_grafana.types.workspace_id
    import aws_sdk_grafana.types.workspace_name
    import aws_sdk_grafana.types.workspace_status


class WorkspaceSummary(TypedDict, closed=True):
    created: "datetime.datetime"
    """<p>The date that the workspace was created.</p>"""
    description: NotRequired["aws_sdk_grafana.types.description.Description"]
    """<p>The customer-entered description of the workspace.</p>"""
    endpoint: "aws_sdk_grafana.types.endpoint.Endpoint"
    """<p>The URL endpoint to use to access the Grafana console in the workspace.</p>"""
    grafana_version: "aws_sdk_grafana.types.grafana_version.GrafanaVersion"
    """<p>The Grafana version that the workspace is running.</p>"""
    id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The unique ID of the workspace.</p>"""
    modified: "datetime.datetime"
    """<p>The most recent date that the workspace was modified.</p>"""
    name: NotRequired["aws_sdk_grafana.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    notification_destinations: NotRequired[
        "aws_sdk_grafana.types.notification_destinations_list.NotificationDestinationsList"
    ]
    """<p>The Amazon Web Services notification channels that Amazon Managed Grafana can automatically create IAM roles and permissions for, which allows Amazon Managed Grafana to use these channels.</p>"""
    status: "aws_sdk_grafana.types.workspace_status.WorkspaceStatus"
    """<p>The current status of the workspace.</p>"""
    authentication: "aws_sdk_grafana.types.authentication_summary.AuthenticationSummary"
    """<p>A structure containing information about the authentication methods used in the workspace.</p>"""
    tags: NotRequired["aws_sdk_grafana.types.tag_map.TagMap"]
    """<p>The list of tags associated with the workspace.</p>"""
    license_type: NotRequired["aws_sdk_grafana.types.license_type.LicenseType"]
    """<p>Specifies whether this workspace has a full Grafana Enterprise license.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>"""
    grafana_token: NotRequired["aws_sdk_grafana.types.grafana_token.GrafanaToken"]
    r"""<p>The token that ties this workspace to a Grafana Labs account. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise\">Link your account with Grafana Labs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummary) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types._prelude.timestamp

    out["created"] = aws_sdk_grafana.types._prelude.timestamp.serialize_json(
        value["created"]
    )
    if "description" in value:
        out["description"] = value["description"]
    out["endpoint"] = value["endpoint"]
    out["grafanaVersion"] = value["grafana_version"]
    out["id"] = value["id"]
    import aws_sdk_grafana.types._prelude.timestamp

    out["modified"] = aws_sdk_grafana.types._prelude.timestamp.serialize_json(
        value["modified"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "notification_destinations" in value:
        import aws_sdk_grafana.types.notification_destinations_list

        out["notificationDestinations"] = (
            aws_sdk_grafana.types.notification_destinations_list.serialize_json(
                value["notification_destinations"]
            )
        )
    out["status"] = value["status"]
    import aws_sdk_grafana.types.authentication_summary

    out["authentication"] = aws_sdk_grafana.types.authentication_summary.serialize_json(
        value["authentication"]
    )
    if "tags" in value:
        import aws_sdk_grafana.types.tag_map

        out["tags"] = aws_sdk_grafana.types.tag_map.serialize_json(value["tags"])
    if "license_type" in value:
        out["licenseType"] = value["license_type"]
    if "grafana_token" in value:
        out["grafanaToken"] = value["grafana_token"]
    return out


def deserialize_json(data: dict) -> WorkspaceSummary:
    out: WorkspaceSummary = {}  # type: ignore[typeddict-item]
    if "created" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["created"] = aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
            data["created"]
        )
    else:
        raise DeserializationError("WorkspaceSummary.created required")
    if "description" in data:
        out["description"] = data["description"]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("WorkspaceSummary.endpoint required")
    if "grafanaVersion" in data:
        out["grafana_version"] = data["grafanaVersion"]
    else:
        raise DeserializationError("WorkspaceSummary.grafana_version required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("WorkspaceSummary.id required")
    if "modified" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["modified"] = aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
            data["modified"]
        )
    else:
        raise DeserializationError("WorkspaceSummary.modified required")
    if "name" in data:
        out["name"] = data["name"]
    if "notificationDestinations" in data:
        import aws_sdk_grafana.types.notification_destinations_list

        out["notification_destinations"] = (
            aws_sdk_grafana.types.notification_destinations_list.deserialize_json(
                data["notificationDestinations"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("WorkspaceSummary.status required")
    if "authentication" in data:
        import aws_sdk_grafana.types.authentication_summary

        out["authentication"] = (
            aws_sdk_grafana.types.authentication_summary.deserialize_json(
                data["authentication"]
            )
        )
    else:
        raise DeserializationError("WorkspaceSummary.authentication required")
    if "tags" in data:
        import aws_sdk_grafana.types.tag_map

        out["tags"] = aws_sdk_grafana.types.tag_map.deserialize_json(data["tags"])
    if "licenseType" in data:
        out["license_type"] = data["licenseType"]
    if "grafanaToken" in data:
        out["grafana_token"] = data["grafanaToken"]
    return out

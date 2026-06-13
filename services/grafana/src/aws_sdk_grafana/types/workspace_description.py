"""Generated from Smithy shape ``com.amazonaws.grafana#WorkspaceDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_grafana.types.account_access_type
    import aws_sdk_grafana.types.authentication_summary
    import aws_sdk_grafana.types.data_source_types_list
    import aws_sdk_grafana.types.degraded_workspace_reason
    import aws_sdk_grafana.types.description
    import aws_sdk_grafana.types.endpoint
    import aws_sdk_grafana.types.grafana_token
    import aws_sdk_grafana.types.grafana_version
    import aws_sdk_grafana.types.iam_role_arn
    import aws_sdk_grafana.types.ip_address_type
    import aws_sdk_grafana.types.kms_key_id
    import aws_sdk_grafana.types.license_type
    import aws_sdk_grafana.types.network_access_configuration
    import aws_sdk_grafana.types.notification_destinations_list
    import aws_sdk_grafana.types.organization_role_name
    import aws_sdk_grafana.types.organizational_unit_list
    import aws_sdk_grafana.types.permission_type
    import aws_sdk_grafana.types.stack_set_name
    import aws_sdk_grafana.types.tag_map
    import aws_sdk_grafana.types.vpc_configuration
    import aws_sdk_grafana.types.workspace_id
    import aws_sdk_grafana.types.workspace_name
    import aws_sdk_grafana.types.workspace_status


class WorkspaceDescription(TypedDict):
    account_access_type: NotRequired[
        "aws_sdk_grafana.types.account_access_type.AccountAccessType"
    ]
    """<p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If this is <code>ORGANIZATION</code>, the <code>workspaceOrganizationalUnits</code> parameter specifies which organizational units the workspace can access.</p>"""
    created: "datetime.datetime"
    """<p>The date that the workspace was created.</p>"""
    data_sources: "aws_sdk_grafana.types.data_source_types_list.DataSourceTypesList"
    """<p>Specifies the Amazon Web Services data sources that have been configured to have IAM roles and permissions created to allow Amazon Managed Grafana to read data from these sources.</p> <p>This list is only used when the workspace was created through the Amazon Web Services console, and the <code>permissionType</code> is <code>SERVICE_MANAGED</code>.</p>"""
    description: NotRequired["aws_sdk_grafana.types.description.Description"]
    """<p>The user-defined description of the workspace.</p>"""
    endpoint: "aws_sdk_grafana.types.endpoint.Endpoint"
    """<p>The URL that users can use to access the Grafana console in the workspace.</p>"""
    grafana_version: "aws_sdk_grafana.types.grafana_version.GrafanaVersion"
    """<p>The version of Grafana supported in this workspace.</p>"""
    id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The unique ID of this workspace.</p>"""
    modified: "datetime.datetime"
    """<p>The most recent date that the workspace was modified.</p>"""
    name: NotRequired["aws_sdk_grafana.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    organization_role_name: NotRequired[
        "aws_sdk_grafana.types.organization_role_name.OrganizationRoleName"
    ]
    """<p>The name of the IAM role that is used to access resources through Organizations.</p>"""
    notification_destinations: NotRequired[
        "aws_sdk_grafana.types.notification_destinations_list.NotificationDestinationsList"
    ]
    """<p>The Amazon Web Services notification channels that Amazon Managed Grafana can automatically create IAM roles and permissions for, to allow Amazon Managed Grafana to use these channels.</p>"""
    organizational_units: NotRequired[
        "aws_sdk_grafana.types.organizational_unit_list.OrganizationalUnitList"
    ]
    """<p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>"""
    permission_type: NotRequired["aws_sdk_grafana.types.permission_type.PermissionType"]
    """<p>If this is <code>SERVICE_MANAGED</code>, and the workplace was created through the Amazon Managed Grafana console, then Amazon Managed Grafana automatically creates the IAM roles and provisions the permissions that the workspace needs to use Amazon Web Services data sources and notification channels.</p> <p>If this is <code>CUSTOMER_MANAGED</code>, you must manage those roles and permissions yourself.</p> <p>If you are working with a workspace in a member account of an organization and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, this parameter must be set to <code>CUSTOMER_MANAGED</code>.</p> <p>For more information about converting between customer and service managed, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html\">Managing permissions for data sources and notification channels</a>. For more information about the roles and permissions that must be managed for customer managed workspaces, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a> </p>"""
    stack_set_name: NotRequired["aws_sdk_grafana.types.stack_set_name.StackSetName"]
    """<p>The name of the CloudFormation stack set that is used to generate IAM roles to be used for this workspace.</p>"""
    status: "aws_sdk_grafana.types.workspace_status.WorkspaceStatus"
    """<p>The current status of the workspace.</p>"""
    workspace_role_arn: NotRequired["aws_sdk_grafana.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role that grants permissions to the Amazon Web Services resources that the workspace will view data from. This role must already exist.</p>"""
    license_type: NotRequired["aws_sdk_grafana.types.license_type.LicenseType"]
    """<p>Specifies whether this workspace has a full Grafana Enterprise license.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>"""
    free_trial_consumed: NotRequired["bool"]
    """<p>Specifies whether this workspace has already fully used its free trial for Grafana Enterprise.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>"""
    license_expiration: NotRequired["datetime.datetime"]
    """<p>If this workspace has a full Grafana Enterprise license purchased through Amazon Web Services Marketplace, this specifies when the license ends and will need to be renewed. Purchasing the Enterprise plugins option through Amazon Managed Grafana does not have an expiration. It is valid until the license is removed.</p>"""
    free_trial_expiration: NotRequired["datetime.datetime"]
    """<p>If this workspace is currently in the free trial period for Grafana Enterprise, this value specifies when that free trial ends.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>"""
    authentication: "aws_sdk_grafana.types.authentication_summary.AuthenticationSummary"
    """<p>A structure that describes whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication.</p>"""
    tags: NotRequired["aws_sdk_grafana.types.tag_map.TagMap"]
    """<p>The list of tags associated with the workspace.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_grafana.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The configuration for connecting to data sources in a private VPC (Amazon Virtual Private Cloud).</p>"""
    network_access_control: NotRequired[
        "aws_sdk_grafana.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    """<p>The configuration settings for network access to your workspace.</p>"""
    grafana_token: NotRequired["aws_sdk_grafana.types.grafana_token.GrafanaToken"]
    """<p>The token that ties this workspace to a Grafana Labs account. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise\">Link your account with Grafana Labs</a>.</p>"""
    ip_address_type: NotRequired["aws_sdk_grafana.types.ip_address_type.IPAddressType"]
    """<p>The type of IP addresses supported for connection to the workspace. Valid values are <code>IPv4</code> and <code>DualStack</code>.</p>"""
    kms_key_id: NotRequired["aws_sdk_grafana.types.kms_key_id.KmsKeyId"]
    """<p>The ID or ARN of the Key Management Service key used for encrypting workspace data.</p>"""
    degraded_workspace_reason: NotRequired[
        "aws_sdk_grafana.types.degraded_workspace_reason.DegradedWorkspaceReason"
    ]
    """<p>If the workspace is in the <code>DEGRADED</code> status, this field describes the reason the workspace is degraded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceDescription) -> dict:
    out: dict = {}
    if "account_access_type" in value:
        out["accountAccessType"] = value["account_access_type"]
    import aws_sdk_grafana.types._prelude.timestamp

    out["created"] = aws_sdk_grafana.types._prelude.timestamp.serialize_json(
        value["created"]
    )
    import aws_sdk_grafana.types.data_source_types_list

    out["dataSources"] = aws_sdk_grafana.types.data_source_types_list.serialize_json(
        value["data_sources"]
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
    if "organization_role_name" in value:
        out["organizationRoleName"] = value["organization_role_name"]
    if "notification_destinations" in value:
        import aws_sdk_grafana.types.notification_destinations_list

        out["notificationDestinations"] = (
            aws_sdk_grafana.types.notification_destinations_list.serialize_json(
                value["notification_destinations"]
            )
        )
    if "organizational_units" in value:
        import aws_sdk_grafana.types.organizational_unit_list

        out["organizationalUnits"] = (
            aws_sdk_grafana.types.organizational_unit_list.serialize_json(
                value["organizational_units"]
            )
        )
    if "permission_type" in value:
        out["permissionType"] = value["permission_type"]
    if "stack_set_name" in value:
        out["stackSetName"] = value["stack_set_name"]
    out["status"] = value["status"]
    if "workspace_role_arn" in value:
        out["workspaceRoleArn"] = value["workspace_role_arn"]
    if "license_type" in value:
        out["licenseType"] = value["license_type"]
    if "free_trial_consumed" in value:
        out["freeTrialConsumed"] = value["free_trial_consumed"]
    if "license_expiration" in value:
        import aws_sdk_grafana.types._prelude.timestamp

        out["licenseExpiration"] = (
            aws_sdk_grafana.types._prelude.timestamp.serialize_json(
                value["license_expiration"]
            )
        )
    if "free_trial_expiration" in value:
        import aws_sdk_grafana.types._prelude.timestamp

        out["freeTrialExpiration"] = (
            aws_sdk_grafana.types._prelude.timestamp.serialize_json(
                value["free_trial_expiration"]
            )
        )
    import aws_sdk_grafana.types.authentication_summary

    out["authentication"] = aws_sdk_grafana.types.authentication_summary.serialize_json(
        value["authentication"]
    )
    if "tags" in value:
        import aws_sdk_grafana.types.tag_map

        out["tags"] = aws_sdk_grafana.types.tag_map.serialize_json(value["tags"])
    if "vpc_configuration" in value:
        import aws_sdk_grafana.types.vpc_configuration

        out["vpcConfiguration"] = (
            aws_sdk_grafana.types.vpc_configuration.serialize_json(
                value["vpc_configuration"]
            )
        )
    if "network_access_control" in value:
        import aws_sdk_grafana.types.network_access_configuration

        out["networkAccessControl"] = (
            aws_sdk_grafana.types.network_access_configuration.serialize_json(
                value["network_access_control"]
            )
        )
    if "grafana_token" in value:
        out["grafanaToken"] = value["grafana_token"]
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "degraded_workspace_reason" in value:
        out["degradedWorkspaceReason"] = value["degraded_workspace_reason"]
    return out


def deserialize_json(data: dict) -> WorkspaceDescription:
    out: WorkspaceDescription = {}  # type: ignore[typeddict-item]
    if "accountAccessType" in data:
        out["account_access_type"] = data["accountAccessType"]
    if "created" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["created"] = aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
            data["created"]
        )
    else:
        raise DeserializationError("WorkspaceDescription.created required")
    if "dataSources" in data:
        import aws_sdk_grafana.types.data_source_types_list

        out["data_sources"] = (
            aws_sdk_grafana.types.data_source_types_list.deserialize_json(
                data["dataSources"]
            )
        )
    else:
        raise DeserializationError("WorkspaceDescription.data_sources required")
    if "description" in data:
        out["description"] = data["description"]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("WorkspaceDescription.endpoint required")
    if "grafanaVersion" in data:
        out["grafana_version"] = data["grafanaVersion"]
    else:
        raise DeserializationError("WorkspaceDescription.grafana_version required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("WorkspaceDescription.id required")
    if "modified" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["modified"] = aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
            data["modified"]
        )
    else:
        raise DeserializationError("WorkspaceDescription.modified required")
    if "name" in data:
        out["name"] = data["name"]
    if "organizationRoleName" in data:
        out["organization_role_name"] = data["organizationRoleName"]
    if "notificationDestinations" in data:
        import aws_sdk_grafana.types.notification_destinations_list

        out["notification_destinations"] = (
            aws_sdk_grafana.types.notification_destinations_list.deserialize_json(
                data["notificationDestinations"]
            )
        )
    if "organizationalUnits" in data:
        import aws_sdk_grafana.types.organizational_unit_list

        out["organizational_units"] = (
            aws_sdk_grafana.types.organizational_unit_list.deserialize_json(
                data["organizationalUnits"]
            )
        )
    if "permissionType" in data:
        out["permission_type"] = data["permissionType"]
    if "stackSetName" in data:
        out["stack_set_name"] = data["stackSetName"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("WorkspaceDescription.status required")
    if "workspaceRoleArn" in data:
        out["workspace_role_arn"] = data["workspaceRoleArn"]
    if "licenseType" in data:
        out["license_type"] = data["licenseType"]
    if "freeTrialConsumed" in data:
        out["free_trial_consumed"] = data["freeTrialConsumed"]
    if "licenseExpiration" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["license_expiration"] = (
            aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
                data["licenseExpiration"]
            )
        )
    if "freeTrialExpiration" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["free_trial_expiration"] = (
            aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
                data["freeTrialExpiration"]
            )
        )
    if "authentication" in data:
        import aws_sdk_grafana.types.authentication_summary

        out["authentication"] = (
            aws_sdk_grafana.types.authentication_summary.deserialize_json(
                data["authentication"]
            )
        )
    else:
        raise DeserializationError("WorkspaceDescription.authentication required")
    if "tags" in data:
        import aws_sdk_grafana.types.tag_map

        out["tags"] = aws_sdk_grafana.types.tag_map.deserialize_json(data["tags"])
    if "vpcConfiguration" in data:
        import aws_sdk_grafana.types.vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_grafana.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    if "networkAccessControl" in data:
        import aws_sdk_grafana.types.network_access_configuration

        out["network_access_control"] = (
            aws_sdk_grafana.types.network_access_configuration.deserialize_json(
                data["networkAccessControl"]
            )
        )
    if "grafanaToken" in data:
        out["grafana_token"] = data["grafanaToken"]
    if "ipAddressType" in data:
        out["ip_address_type"] = data["ipAddressType"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "degradedWorkspaceReason" in data:
        out["degraded_workspace_reason"] = data["degradedWorkspaceReason"]
    return out

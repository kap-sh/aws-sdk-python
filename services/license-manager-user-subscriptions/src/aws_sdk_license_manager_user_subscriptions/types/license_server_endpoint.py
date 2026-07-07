"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#LicenseServerEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_license_manager_user_subscriptions.types.arn
    import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_id
    import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_provisioning_status
    import aws_sdk_license_manager_user_subscriptions.types.license_server_list
    import aws_sdk_license_manager_user_subscriptions.types.server_endpoint
    import aws_sdk_license_manager_user_subscriptions.types.server_type


class LicenseServerEndpoint(TypedDict, closed=True):
    identity_provider_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the identity provider that's associated with the RDS license server endpoint.</p>"""
    server_type: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.server_type.ServerType"
    ]
    """<p>The type of license server.</p>"""
    server_endpoint: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.server_endpoint.ServerEndpoint"
    ]
    """<p>The <code>ServerEndpoint</code> resource contains the network address of the RDS license server endpoint.</p>"""
    status_message: NotRequired["str"]
    """<p>The message associated with the provisioning status, if there is one.</p>"""
    license_server_endpoint_id: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_id.LicenseServerEndpointId"
    ]
    """<p>The ID of the license server endpoint.</p>"""
    license_server_endpoint_arn: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The ARN of the <code>ServerEndpoint</code> resource for the RDS license server.</p>"""
    license_server_endpoint_provisioning_status: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_provisioning_status.LicenseServerEndpointProvisioningStatus"
    ]
    """<p>The current state of the provisioning process for the RDS license server endpoint</p>"""
    license_servers: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.license_server_list.LicenseServerList"
    ]
    """<p>An array of <code>LicenseServer</code> resources that represent the license servers that are accessed through this endpoint.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when License Manager created the license server endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseServerEndpoint) -> dict:
    out: dict = {}
    if "identity_provider_arn" in value:
        out["IdentityProviderArn"] = value["identity_provider_arn"]
    if "server_type" in value:
        out["ServerType"] = value["server_type"]
    if "server_endpoint" in value:
        import aws_sdk_license_manager_user_subscriptions.types.server_endpoint

        out["ServerEndpoint"] = (
            aws_sdk_license_manager_user_subscriptions.types.server_endpoint.serialize_json(
                value["server_endpoint"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "license_server_endpoint_id" in value:
        out["LicenseServerEndpointId"] = value["license_server_endpoint_id"]
    if "license_server_endpoint_arn" in value:
        out["LicenseServerEndpointArn"] = value["license_server_endpoint_arn"]
    if "license_server_endpoint_provisioning_status" in value:
        out["LicenseServerEndpointProvisioningStatus"] = value[
            "license_server_endpoint_provisioning_status"
        ]
    if "license_servers" in value:
        import aws_sdk_license_manager_user_subscriptions.types.license_server_list

        out["LicenseServers"] = (
            aws_sdk_license_manager_user_subscriptions.types.license_server_list.serialize_json(
                value["license_servers"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_license_manager_user_subscriptions.types._prelude.timestamp

        out["CreationTime"] = (
            aws_sdk_license_manager_user_subscriptions.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> LicenseServerEndpoint:
    out: LicenseServerEndpoint = {}  # type: ignore[typeddict-item]
    if "IdentityProviderArn" in data:
        out["identity_provider_arn"] = data["IdentityProviderArn"]
    if "ServerType" in data:
        out["server_type"] = data["ServerType"]
    if "ServerEndpoint" in data:
        import aws_sdk_license_manager_user_subscriptions.types.server_endpoint

        out["server_endpoint"] = (
            aws_sdk_license_manager_user_subscriptions.types.server_endpoint.deserialize_json(
                data["ServerEndpoint"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "LicenseServerEndpointId" in data:
        out["license_server_endpoint_id"] = data["LicenseServerEndpointId"]
    if "LicenseServerEndpointArn" in data:
        out["license_server_endpoint_arn"] = data["LicenseServerEndpointArn"]
    if "LicenseServerEndpointProvisioningStatus" in data:
        out["license_server_endpoint_provisioning_status"] = data[
            "LicenseServerEndpointProvisioningStatus"
        ]
    if "LicenseServers" in data:
        import aws_sdk_license_manager_user_subscriptions.types.license_server_list

        out["license_servers"] = (
            aws_sdk_license_manager_user_subscriptions.types.license_server_list.deserialize_json(
                data["LicenseServers"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_license_manager_user_subscriptions.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_license_manager_user_subscriptions.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    return out

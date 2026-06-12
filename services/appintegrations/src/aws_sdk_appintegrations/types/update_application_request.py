"""Generated from Smithy shape ``com.amazonaws.appintegrations#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_config
    import aws_sdk_appintegrations.types.application_name
    import aws_sdk_appintegrations.types.application_source_config
    import aws_sdk_appintegrations.types.application_type
    import aws_sdk_appintegrations.types.arn_or_uuid
    import aws_sdk_appintegrations.types.boolean
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.iframe_config
    import aws_sdk_appintegrations.types.initialization_timeout
    import aws_sdk_appintegrations.types.permission_list
    import aws_sdk_appintegrations.types.publication_list
    import aws_sdk_appintegrations.types.subscription_list


class UpdateApplicationRequest(TypedDict):
    arn: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID"
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    name: NotRequired["aws_sdk_appintegrations.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>The description of the application.</p>"""
    application_source_config: NotRequired[
        "aws_sdk_appintegrations.types.application_source_config.ApplicationSourceConfig"
    ]
    """<p>The configuration for where the application should be loaded from.</p>"""
    subscriptions: NotRequired[
        "aws_sdk_appintegrations.types.subscription_list.SubscriptionList"
    ]
    """<p>The events that the application subscribes.</p>"""
    publications: NotRequired[
        "aws_sdk_appintegrations.types.publication_list.PublicationList"
    ]
    """<p>The events that the application publishes.</p>"""
    permissions: NotRequired[
        "aws_sdk_appintegrations.types.permission_list.PermissionList"
    ]
    """<p>The configuration of events or requests that the application has access to.</p>"""
    is_service: NotRequired["aws_sdk_appintegrations.types.boolean.Boolean"]
    """<p>Indicates whether the application is a service.</p>"""
    initialization_timeout: NotRequired[
        "aws_sdk_appintegrations.types.initialization_timeout.InitializationTimeout"
    ]
    """<p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>"""
    application_config: NotRequired[
        "aws_sdk_appintegrations.types.application_config.ApplicationConfig"
    ]
    """<p>The configuration settings for the application.</p>"""
    iframe_config: NotRequired[
        "aws_sdk_appintegrations.types.iframe_config.IframeConfig"
    ]
    """<p>The iframe configuration for the application.</p>"""
    application_type: NotRequired[
        "aws_sdk_appintegrations.types.application_type.ApplicationType"
    ]
    """<p>The type of application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "application_source_config" in value:
        import aws_sdk_appintegrations.types.application_source_config

        out["ApplicationSourceConfig"] = (
            aws_sdk_appintegrations.types.application_source_config.serialize_json(
                value["application_source_config"]
            )
        )
    if "subscriptions" in value:
        import aws_sdk_appintegrations.types.subscription_list

        out["Subscriptions"] = (
            aws_sdk_appintegrations.types.subscription_list.serialize_json(
                value["subscriptions"]
            )
        )
    if "publications" in value:
        import aws_sdk_appintegrations.types.publication_list

        out["Publications"] = (
            aws_sdk_appintegrations.types.publication_list.serialize_json(
                value["publications"]
            )
        )
    if "permissions" in value:
        import aws_sdk_appintegrations.types.permission_list

        out["Permissions"] = (
            aws_sdk_appintegrations.types.permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "is_service" in value:
        out["IsService"] = value["is_service"]
    if "initialization_timeout" in value:
        out["InitializationTimeout"] = value["initialization_timeout"]
    if "application_config" in value:
        import aws_sdk_appintegrations.types.application_config

        out["ApplicationConfig"] = (
            aws_sdk_appintegrations.types.application_config.serialize_json(
                value["application_config"]
            )
        )
    if "iframe_config" in value:
        import aws_sdk_appintegrations.types.iframe_config

        out["IframeConfig"] = (
            aws_sdk_appintegrations.types.iframe_config.serialize_json(
                value["iframe_config"]
            )
        )
    if "application_type" in value:
        import aws_sdk_appintegrations.types.application_type

        out["ApplicationType"] = (
            aws_sdk_appintegrations.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ApplicationSourceConfig" in data:
        import aws_sdk_appintegrations.types.application_source_config

        out["application_source_config"] = (
            aws_sdk_appintegrations.types.application_source_config.deserialize_json(
                data["ApplicationSourceConfig"]
            )
        )
    if "Subscriptions" in data:
        import aws_sdk_appintegrations.types.subscription_list

        out["subscriptions"] = (
            aws_sdk_appintegrations.types.subscription_list.deserialize_json(
                data["Subscriptions"]
            )
        )
    if "Publications" in data:
        import aws_sdk_appintegrations.types.publication_list

        out["publications"] = (
            aws_sdk_appintegrations.types.publication_list.deserialize_json(
                data["Publications"]
            )
        )
    if "Permissions" in data:
        import aws_sdk_appintegrations.types.permission_list

        out["permissions"] = (
            aws_sdk_appintegrations.types.permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "IsService" in data:
        out["is_service"] = data["IsService"]
    if "InitializationTimeout" in data:
        out["initialization_timeout"] = data["InitializationTimeout"]
    if "ApplicationConfig" in data:
        import aws_sdk_appintegrations.types.application_config

        out["application_config"] = (
            aws_sdk_appintegrations.types.application_config.deserialize_json(
                data["ApplicationConfig"]
            )
        )
    if "IframeConfig" in data:
        import aws_sdk_appintegrations.types.iframe_config

        out["iframe_config"] = (
            aws_sdk_appintegrations.types.iframe_config.deserialize_json(
                data["IframeConfig"]
            )
        )
    if "ApplicationType" in data:
        import aws_sdk_appintegrations.types.application_type

        out["application_type"] = (
            aws_sdk_appintegrations.types.application_type.deserialize_json(
                data["ApplicationType"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_config
    import aws_sdk_appintegrations.types.application_name
    import aws_sdk_appintegrations.types.application_namespace
    import aws_sdk_appintegrations.types.application_source_config
    import aws_sdk_appintegrations.types.application_type
    import aws_sdk_appintegrations.types.boolean
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.idempotency_token
    import aws_sdk_appintegrations.types.iframe_config
    import aws_sdk_appintegrations.types.initialization_timeout
    import aws_sdk_appintegrations.types.permission_list
    import aws_sdk_appintegrations.types.publication_list
    import aws_sdk_appintegrations.types.subscription_list
    import aws_sdk_appintegrations.types.tag_map


class CreateApplicationRequest(TypedDict):
    name: "aws_sdk_appintegrations.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    namespace: (
        "aws_sdk_appintegrations.types.application_namespace.ApplicationNamespace"
    )
    """<p>The namespace of the application.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>The description of the application.</p>"""
    application_source_config: "aws_sdk_appintegrations.types.application_source_config.ApplicationSourceConfig"
    """<p>The configuration for where the application should be loaded from.</p>"""
    subscriptions: NotRequired[
        "aws_sdk_appintegrations.types.subscription_list.SubscriptionList"
    ]
    """<p>The events that the application subscribes.</p>"""
    publications: NotRequired[
        "aws_sdk_appintegrations.types.publication_list.PublicationList"
    ]
    """<p>The events that the application publishes.</p>"""
    client_token: NotRequired[
        "aws_sdk_appintegrations.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["aws_sdk_appintegrations.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    permissions: NotRequired[
        "aws_sdk_appintegrations.types.permission_list.PermissionList"
    ]
    """<p>The configuration of events or requests that the application has access to.</p>"""
    is_service: "aws_sdk_appintegrations.types.boolean.Boolean"
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
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Namespace"] = value["namespace"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_appintegrations.types.tag_map

        out["Tags"] = aws_sdk_appintegrations.types.tag_map.serialize_json(
            value["tags"]
        )
    if "permissions" in value:
        import aws_sdk_appintegrations.types.permission_list

        out["Permissions"] = (
            aws_sdk_appintegrations.types.permission_list.serialize_json(
                value["permissions"]
            )
        )
    out["IsService"] = value.get("is_service", False)
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


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError("CreateApplicationRequest.namespace required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ApplicationSourceConfig" in data:
        import aws_sdk_appintegrations.types.application_source_config

        out["application_source_config"] = (
            aws_sdk_appintegrations.types.application_source_config.deserialize_json(
                data["ApplicationSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApplicationRequest.application_source_config required"
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
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_appintegrations.types.tag_map

        out["tags"] = aws_sdk_appintegrations.types.tag_map.deserialize_json(
            data["Tags"]
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
    else:
        out["is_service"] = False
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

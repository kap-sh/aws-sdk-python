"""Generated from Smithy shape ``com.amazonaws.appintegrations#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.application_config
    import capo_appintegrations.types.application_name
    import capo_appintegrations.types.application_namespace
    import capo_appintegrations.types.application_source_config
    import capo_appintegrations.types.application_type
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.boolean
    import capo_appintegrations.types.description
    import capo_appintegrations.types.iframe_config
    import capo_appintegrations.types.initialization_timeout
    import capo_appintegrations.types.permission_list
    import capo_appintegrations.types.publication_list
    import capo_appintegrations.types.subscription_list
    import capo_appintegrations.types.tag_map
    import capo_appintegrations.types.timestamp
    import capo_appintegrations.types.uuid


class GetApplicationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    id: NotRequired["capo_appintegrations.types.uuid.UUID"]
    """<p>A unique identifier for the Application.</p>"""
    name: NotRequired["capo_appintegrations.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    namespace: NotRequired[
        "capo_appintegrations.types.application_namespace.ApplicationNamespace"
    ]
    """<p>The namespace of the application.</p>"""
    description: NotRequired["capo_appintegrations.types.description.Description"]
    """<p>The description of the application.</p>"""
    application_source_config: NotRequired[
        "capo_appintegrations.types.application_source_config.ApplicationSourceConfig"
    ]
    """<p>The configuration for where the application should be loaded from.</p>"""
    subscriptions: NotRequired[
        "capo_appintegrations.types.subscription_list.SubscriptionList"
    ]
    """<p>The events that the application subscribes.</p>"""
    publications: NotRequired[
        "capo_appintegrations.types.publication_list.PublicationList"
    ]
    """<p>The events that the application publishes.</p>"""
    created_time: NotRequired["capo_appintegrations.types.timestamp.Timestamp"]
    """<p>The created time of the Application.</p>"""
    last_modified_time: NotRequired["capo_appintegrations.types.timestamp.Timestamp"]
    """<p>The last modified time of the Application.</p>"""
    tags: NotRequired["capo_appintegrations.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    permissions: NotRequired[
        "capo_appintegrations.types.permission_list.PermissionList"
    ]
    """<p>The configuration of events or requests that the application has access to.</p>"""
    is_service: "capo_appintegrations.types.boolean.Boolean"
    """<p>Indicates whether the application is a service.</p>"""
    initialization_timeout: NotRequired[
        "capo_appintegrations.types.initialization_timeout.InitializationTimeout"
    ]
    """<p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>"""
    application_config: NotRequired[
        "capo_appintegrations.types.application_config.ApplicationConfig"
    ]
    """<p>The configuration settings for the application.</p>"""
    iframe_config: NotRequired["capo_appintegrations.types.iframe_config.IframeConfig"]
    """<p>The iframe configuration for the application.</p>"""
    application_type: NotRequired[
        "capo_appintegrations.types.application_type.ApplicationType"
    ]
    """<p>The type of application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "description" in value:
        out["Description"] = value["description"]
    if "application_source_config" in value:
        import capo_appintegrations.types.application_source_config

        out["ApplicationSourceConfig"] = (
            capo_appintegrations.types.application_source_config.serialize_json(
                value["application_source_config"]
            )
        )
    if "subscriptions" in value:
        import capo_appintegrations.types.subscription_list

        out["Subscriptions"] = (
            capo_appintegrations.types.subscription_list.serialize_json(
                value["subscriptions"]
            )
        )
    if "publications" in value:
        import capo_appintegrations.types.publication_list

        out["Publications"] = (
            capo_appintegrations.types.publication_list.serialize_json(
                value["publications"]
            )
        )
    if "created_time" in value:
        import capo_appintegrations.types.timestamp

        out["CreatedTime"] = capo_appintegrations.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import capo_appintegrations.types.timestamp

        out["LastModifiedTime"] = capo_appintegrations.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "tags" in value:
        import capo_appintegrations.types.tag_map

        out["Tags"] = capo_appintegrations.types.tag_map.serialize_json(value["tags"])
    if "permissions" in value:
        import capo_appintegrations.types.permission_list

        out["Permissions"] = capo_appintegrations.types.permission_list.serialize_json(
            value["permissions"]
        )
    out["IsService"] = value.get("is_service", False)
    if "initialization_timeout" in value:
        out["InitializationTimeout"] = value["initialization_timeout"]
    if "application_config" in value:
        import capo_appintegrations.types.application_config

        out["ApplicationConfig"] = (
            capo_appintegrations.types.application_config.serialize_json(
                value["application_config"]
            )
        )
    if "iframe_config" in value:
        import capo_appintegrations.types.iframe_config

        out["IframeConfig"] = capo_appintegrations.types.iframe_config.serialize_json(
            value["iframe_config"]
        )
    if "application_type" in value:
        import capo_appintegrations.types.application_type

        out["ApplicationType"] = (
            capo_appintegrations.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ApplicationSourceConfig" in data:
        import capo_appintegrations.types.application_source_config

        out["application_source_config"] = (
            capo_appintegrations.types.application_source_config.deserialize_json(
                data["ApplicationSourceConfig"]
            )
        )
    if "Subscriptions" in data:
        import capo_appintegrations.types.subscription_list

        out["subscriptions"] = (
            capo_appintegrations.types.subscription_list.deserialize_json(
                data["Subscriptions"]
            )
        )
    if "Publications" in data:
        import capo_appintegrations.types.publication_list

        out["publications"] = (
            capo_appintegrations.types.publication_list.deserialize_json(
                data["Publications"]
            )
        )
    if "CreatedTime" in data:
        import capo_appintegrations.types.timestamp

        out["created_time"] = capo_appintegrations.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastModifiedTime" in data:
        import capo_appintegrations.types.timestamp

        out["last_modified_time"] = (
            capo_appintegrations.types.timestamp.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if "Tags" in data:
        import capo_appintegrations.types.tag_map

        out["tags"] = capo_appintegrations.types.tag_map.deserialize_json(data["Tags"])
    if "Permissions" in data:
        import capo_appintegrations.types.permission_list

        out["permissions"] = (
            capo_appintegrations.types.permission_list.deserialize_json(
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
        import capo_appintegrations.types.application_config

        out["application_config"] = (
            capo_appintegrations.types.application_config.deserialize_json(
                data["ApplicationConfig"]
            )
        )
    if "IframeConfig" in data:
        import capo_appintegrations.types.iframe_config

        out["iframe_config"] = (
            capo_appintegrations.types.iframe_config.deserialize_json(
                data["IframeConfig"]
            )
        )
    if "ApplicationType" in data:
        import capo_appintegrations.types.application_type

        out["application_type"] = (
            capo_appintegrations.types.application_type.deserialize_json(
                data["ApplicationType"]
            )
        )
    return out

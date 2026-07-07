"""Generated from Smithy shape ``com.amazonaws.connect#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.application_permissions
    import aws_sdk_connect.types.application_type
    import aws_sdk_connect.types.namespace


class Application(TypedDict, closed=True):
    namespace: NotRequired["aws_sdk_connect.types.namespace.Namespace"]
    """<p>Namespace of the application that you want to give access to.</p>"""
    application_permissions: NotRequired[
        "aws_sdk_connect.types.application_permissions.ApplicationPermissions"
    ]
    """<p>The permissions that the agent is granted on the application. For third-party applications, only the <code>ACCESS</code> permission is supported. For MCP Servers, the permissions are tool Identifiers accepted by MCP Server. </p>"""
    type: NotRequired["aws_sdk_connect.types.application_type.ApplicationType"]
    """<p> Type of Application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "application_permissions" in value:
        import aws_sdk_connect.types.application_permissions

        out["ApplicationPermissions"] = (
            aws_sdk_connect.types.application_permissions.serialize_json(
                value["application_permissions"]
            )
        )
    if "type" in value:
        import aws_sdk_connect.types.application_type

        out["Type"] = aws_sdk_connect.types.application_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "ApplicationPermissions" in data:
        import aws_sdk_connect.types.application_permissions

        out["application_permissions"] = (
            aws_sdk_connect.types.application_permissions.deserialize_json(
                data["ApplicationPermissions"]
            )
        )
    if "Type" in data:
        import aws_sdk_connect.types.application_type

        out["type"] = aws_sdk_connect.types.application_type.deserialize_json(
            data["Type"]
        )
    return out

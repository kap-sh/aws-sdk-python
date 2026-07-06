"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_name
    import aws_sdk_appintegrations.types.application_namespace
    import aws_sdk_appintegrations.types.application_type
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.boolean
    import aws_sdk_appintegrations.types.timestamp
    import aws_sdk_appintegrations.types.uuid


class ApplicationSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    id: NotRequired["aws_sdk_appintegrations.types.uuid.UUID"]
    """<p>A unique identifier for the Application.</p>"""
    name: NotRequired["aws_sdk_appintegrations.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    namespace: NotRequired[
        "aws_sdk_appintegrations.types.application_namespace.ApplicationNamespace"
    ]
    """<p>The namespace of the application.</p>"""
    created_time: NotRequired["aws_sdk_appintegrations.types.timestamp.Timestamp"]
    """<p>The time when the application was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_appintegrations.types.timestamp.Timestamp"]
    """<p>The time when the application was last modified.</p>"""
    is_service: "aws_sdk_appintegrations.types.boolean.Boolean"
    """<p>Indicates whether the application is a service.</p>"""
    application_type: NotRequired[
        "aws_sdk_appintegrations.types.application_type.ApplicationType"
    ]
    """<p>The type of application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "created_time" in value:
        import aws_sdk_appintegrations.types.timestamp

        out["CreatedTime"] = aws_sdk_appintegrations.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_appintegrations.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_appintegrations.types.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    out["IsService"] = value.get("is_service", False)
    if "application_type" in value:
        import aws_sdk_appintegrations.types.application_type

        out["ApplicationType"] = (
            aws_sdk_appintegrations.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "CreatedTime" in data:
        import aws_sdk_appintegrations.types.timestamp

        out["created_time"] = aws_sdk_appintegrations.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_appintegrations.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_appintegrations.types.timestamp.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if "IsService" in data:
        out["is_service"] = data["IsService"]
    else:
        out["is_service"] = False
    if "ApplicationType" in data:
        import aws_sdk_appintegrations.types.application_type

        out["application_type"] = (
            aws_sdk_appintegrations.types.application_type.deserialize_json(
                data["ApplicationType"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.workdocs#AddResourcePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.notification_options
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.share_principal_list


class AddResourcePermissionsRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    principals: "aws_sdk_workdocs.types.share_principal_list.SharePrincipalList"
    """<p>The users, groups, or organization being granted permission.</p>"""
    notification_options: NotRequired[
        "aws_sdk_workdocs.types.notification_options.NotificationOptions"
    ]
    """<p>The notification options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddResourcePermissionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_workdocs.types.share_principal_list

    out["Principals"] = aws_sdk_workdocs.types.share_principal_list.serialize_json(
        value["principals"]
    )
    if "notification_options" in value:
        import aws_sdk_workdocs.types.notification_options

        out["NotificationOptions"] = (
            aws_sdk_workdocs.types.notification_options.serialize_json(
                value["notification_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddResourcePermissionsRequest:
    out: AddResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "Principals" in data:
        import aws_sdk_workdocs.types.share_principal_list

        out["principals"] = (
            aws_sdk_workdocs.types.share_principal_list.deserialize_json(
                data["Principals"]
            )
        )
    else:
        raise DeserializationError("AddResourcePermissionsRequest.principals required")
    if "NotificationOptions" in data:
        import aws_sdk_workdocs.types.notification_options

        out["notification_options"] = (
            aws_sdk_workdocs.types.notification_options.deserialize_json(
                data["NotificationOptions"]
            )
        )
    return out

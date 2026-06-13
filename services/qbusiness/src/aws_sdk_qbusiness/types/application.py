"""Generated from Smithy shape ``com.amazonaws.qbusiness#Application``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.application_name
    import aws_sdk_qbusiness.types.application_status
    import aws_sdk_qbusiness.types.identity_type
    import aws_sdk_qbusiness.types.quick_sight_configuration
    import aws_sdk_qbusiness.types.timestamp


class Application(TypedDict):
    display_name: NotRequired[
        "aws_sdk_qbusiness.types.application_name.ApplicationName"
    ]
    """<p>The name of the Amazon Q Business application.</p>"""
    application_id: NotRequired["aws_sdk_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier for the Amazon Q Business application.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business application was last updated. </p>"""
    status: NotRequired["aws_sdk_qbusiness.types.application_status.ApplicationStatus"]
    """<p>The status of the Amazon Q Business application. The application is ready to use when the status is <code>ACTIVE</code>.</p>"""
    identity_type: NotRequired["aws_sdk_qbusiness.types.identity_type.IdentityType"]
    """<p>The authentication type being used by a Amazon Q Business application.</p>"""
    quick_sight_configuration: NotRequired[
        "aws_sdk_qbusiness.types.quick_sight_configuration.QuickSightConfiguration"
    ]
    """<p>The Amazon Quick Suite configuration for an Amazon Q Business application that uses Quick Suite as the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "status" in value:
        import aws_sdk_qbusiness.types.application_status

        out["status"] = aws_sdk_qbusiness.types.application_status.serialize_json(
            value["status"]
        )
    if "identity_type" in value:
        import aws_sdk_qbusiness.types.identity_type

        out["identityType"] = aws_sdk_qbusiness.types.identity_type.serialize_json(
            value["identity_type"]
        )
    if "quick_sight_configuration" in value:
        import aws_sdk_qbusiness.types.quick_sight_configuration

        out["quickSightConfiguration"] = (
            aws_sdk_qbusiness.types.quick_sight_configuration.serialize_json(
                value["quick_sight_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "status" in data:
        import aws_sdk_qbusiness.types.application_status

        out["status"] = aws_sdk_qbusiness.types.application_status.deserialize_json(
            data["status"]
        )
    if "identityType" in data:
        import aws_sdk_qbusiness.types.identity_type

        out["identity_type"] = aws_sdk_qbusiness.types.identity_type.deserialize_json(
            data["identityType"]
        )
    if "quickSightConfiguration" in data:
        import aws_sdk_qbusiness.types.quick_sight_configuration

        out["quick_sight_configuration"] = (
            aws_sdk_qbusiness.types.quick_sight_configuration.deserialize_json(
                data["quickSightConfiguration"]
            )
        )
    return out

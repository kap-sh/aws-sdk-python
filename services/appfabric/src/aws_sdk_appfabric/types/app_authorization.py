"""Generated from Smithy shape ``com.amazonaws.appfabric#AppAuthorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_authorization_status
    import aws_sdk_appfabric.types.arn
    import aws_sdk_appfabric.types.auth_type
    import aws_sdk_appfabric.types.date_time
    import aws_sdk_appfabric.types.persona
    import aws_sdk_appfabric.types.string255
    import aws_sdk_appfabric.types.tenant


class AppAuthorization(TypedDict, closed=True):
    app_authorization_arn: "aws_sdk_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app authorization.</p>"""
    app_bundle_arn: "aws_sdk_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app bundle for the app authorization.</p>"""
    app: "aws_sdk_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant: "aws_sdk_appfabric.types.tenant.Tenant"
    """<p>Contains information about an application tenant, such as the application display name and identifier.</p>"""
    auth_type: "aws_sdk_appfabric.types.auth_type.AuthType"
    """<p>The authorization type.</p>"""
    status: "aws_sdk_appfabric.types.app_authorization_status.AppAuthorizationStatus"
    """<p>The state of the app authorization.</p> <p>The following states are possible:</p> <ul> <li> <p> <code>PendingConnect</code>: The initial state of the app authorization. The app authorization is created but not yet connected.</p> </li> <li> <p> <code>Connected</code>: The app authorization is connected to the application, and is ready to be used.</p> </li> <li> <p> <code>ConnectionValidationFailed</code>: The app authorization received a validation exception when trying to connect to the application. If the app authorization is in this state, you should verify the configured credentials and try to connect the app authorization again.</p> </li> <li> <p> <code>TokenAutoRotationFailed</code>: AppFabric failed to refresh the access token. If the app authorization is in this state, you should try to reconnect the app authorization.</p> </li> </ul>"""
    created_at: "aws_sdk_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the app authorization was created.</p>"""
    updated_at: "aws_sdk_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the app authorization was last updated.</p>"""
    persona: NotRequired["aws_sdk_appfabric.types.persona.Persona"]
    """<p>The user persona of the app authorization.</p> <p>This field should always be <code>admin</code>.</p>"""
    auth_url: NotRequired["str"]
    """<p>The application URL for the OAuth flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppAuthorization) -> dict:
    out: dict = {}
    out["appAuthorizationArn"] = value["app_authorization_arn"]
    out["appBundleArn"] = value["app_bundle_arn"]
    out["app"] = value["app"]
    import aws_sdk_appfabric.types.tenant

    out["tenant"] = aws_sdk_appfabric.types.tenant.serialize_json(value["tenant"])
    import aws_sdk_appfabric.types.auth_type

    out["authType"] = aws_sdk_appfabric.types.auth_type.serialize_json(
        value["auth_type"]
    )
    import aws_sdk_appfabric.types.app_authorization_status

    out["status"] = aws_sdk_appfabric.types.app_authorization_status.serialize_json(
        value["status"]
    )
    import aws_sdk_appfabric.types.date_time

    out["createdAt"] = aws_sdk_appfabric.types.date_time.serialize_json(
        value["created_at"]
    )
    import aws_sdk_appfabric.types.date_time

    out["updatedAt"] = aws_sdk_appfabric.types.date_time.serialize_json(
        value["updated_at"]
    )
    if "persona" in value:
        import aws_sdk_appfabric.types.persona

        out["persona"] = aws_sdk_appfabric.types.persona.serialize_json(
            value["persona"]
        )
    if "auth_url" in value:
        out["authUrl"] = value["auth_url"]
    return out


def deserialize_json(data: dict) -> AppAuthorization:
    out: AppAuthorization = {}  # type: ignore[typeddict-item]
    if "appAuthorizationArn" in data:
        out["app_authorization_arn"] = data["appAuthorizationArn"]
    else:
        raise DeserializationError("AppAuthorization.app_authorization_arn required")
    if "appBundleArn" in data:
        out["app_bundle_arn"] = data["appBundleArn"]
    else:
        raise DeserializationError("AppAuthorization.app_bundle_arn required")
    if "app" in data:
        out["app"] = data["app"]
    else:
        raise DeserializationError("AppAuthorization.app required")
    if "tenant" in data:
        import aws_sdk_appfabric.types.tenant

        out["tenant"] = aws_sdk_appfabric.types.tenant.deserialize_json(data["tenant"])
    else:
        raise DeserializationError("AppAuthorization.tenant required")
    if "authType" in data:
        import aws_sdk_appfabric.types.auth_type

        out["auth_type"] = aws_sdk_appfabric.types.auth_type.deserialize_json(
            data["authType"]
        )
    else:
        raise DeserializationError("AppAuthorization.auth_type required")
    if "status" in data:
        import aws_sdk_appfabric.types.app_authorization_status

        out["status"] = (
            aws_sdk_appfabric.types.app_authorization_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AppAuthorization.status required")
    if "createdAt" in data:
        import aws_sdk_appfabric.types.date_time

        out["created_at"] = aws_sdk_appfabric.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AppAuthorization.created_at required")
    if "updatedAt" in data:
        import aws_sdk_appfabric.types.date_time

        out["updated_at"] = aws_sdk_appfabric.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AppAuthorization.updated_at required")
    if "persona" in data:
        import aws_sdk_appfabric.types.persona

        out["persona"] = aws_sdk_appfabric.types.persona.deserialize_json(
            data["persona"]
        )
    if "authUrl" in data:
        out["auth_url"] = data["authUrl"]
    return out

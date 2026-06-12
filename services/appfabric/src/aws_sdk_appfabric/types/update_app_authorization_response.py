"""Generated from Smithy shape ``com.amazonaws.appfabric#UpdateAppAuthorizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_authorization


class UpdateAppAuthorizationResponse(TypedDict):
    app_authorization: "aws_sdk_appfabric.types.app_authorization.AppAuthorization"
    """<p>Contains information about an app authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppAuthorizationResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.app_authorization

    out["appAuthorization"] = aws_sdk_appfabric.types.app_authorization.serialize_json(
        value["app_authorization"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAppAuthorizationResponse:
    out: UpdateAppAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "appAuthorization" in data:
        import aws_sdk_appfabric.types.app_authorization

        out["app_authorization"] = (
            aws_sdk_appfabric.types.app_authorization.deserialize_json(
                data["appAuthorization"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAppAuthorizationResponse.app_authorization required"
        )
    return out

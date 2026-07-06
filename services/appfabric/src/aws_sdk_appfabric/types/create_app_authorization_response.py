"""Generated from Smithy shape ``com.amazonaws.appfabric#CreateAppAuthorizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_authorization


class CreateAppAuthorizationResponse(TypedDict, closed=True):
    app_authorization: "aws_sdk_appfabric.types.app_authorization.AppAuthorization"
    """<p>Contains information about an app authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppAuthorizationResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.app_authorization

    out["appAuthorization"] = aws_sdk_appfabric.types.app_authorization.serialize_json(
        value["app_authorization"]
    )
    return out


def deserialize_json(data: dict) -> CreateAppAuthorizationResponse:
    out: CreateAppAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "appAuthorization" in data:
        import aws_sdk_appfabric.types.app_authorization

        out["app_authorization"] = (
            aws_sdk_appfabric.types.app_authorization.deserialize_json(
                data["appAuthorization"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAppAuthorizationResponse.app_authorization required"
        )
    return out

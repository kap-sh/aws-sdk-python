"""Generated from Smithy shape ``com.amazonaws.appfabric#GetAppAuthorizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_authorization


class GetAppAuthorizationResponse(TypedDict):
    app_authorization: "aws_sdk_appfabric.types.app_authorization.AppAuthorization"
    """<p>Contains information about an app authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppAuthorizationResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.app_authorization

    out["appAuthorization"] = aws_sdk_appfabric.types.app_authorization.serialize_json(
        value["app_authorization"]
    )
    return out


def deserialize_json(data: dict) -> GetAppAuthorizationResponse:
    out: GetAppAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "appAuthorization" in data:
        import aws_sdk_appfabric.types.app_authorization

        out["app_authorization"] = (
            aws_sdk_appfabric.types.app_authorization.deserialize_json(
                data["appAuthorization"]
            )
        )
    else:
        raise DeserializationError(
            "GetAppAuthorizationResponse.app_authorization required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.appfabric#GetAppAuthorizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.app_authorization


class GetAppAuthorizationResponse(TypedDict, closed=True):
    app_authorization: "capo_appfabric.types.app_authorization.AppAuthorization"
    """<p>Contains information about an app authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppAuthorizationResponse) -> dict:
    out: dict = {}
    import capo_appfabric.types.app_authorization

    out["appAuthorization"] = capo_appfabric.types.app_authorization.serialize_json(
        value["app_authorization"]
    )
    return out


def deserialize_json(data: dict) -> GetAppAuthorizationResponse:
    out: GetAppAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "appAuthorization" in data:
        import capo_appfabric.types.app_authorization

        out["app_authorization"] = (
            capo_appfabric.types.app_authorization.deserialize_json(
                data["appAuthorization"]
            )
        )
    else:
        raise DeserializationError(
            "GetAppAuthorizationResponse.app_authorization required"
        )
    return out

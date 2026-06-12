"""Generated from Smithy shape ``com.amazonaws.appfabric#ConnectAppAuthorizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_authorization_summary


class ConnectAppAuthorizationResponse(TypedDict):
    app_authorization_summary: (
        "aws_sdk_appfabric.types.app_authorization_summary.AppAuthorizationSummary"
    )
    """<p>Contains a summary of the app authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectAppAuthorizationResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.app_authorization_summary

    out["appAuthorizationSummary"] = (
        aws_sdk_appfabric.types.app_authorization_summary.serialize_json(
            value["app_authorization_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConnectAppAuthorizationResponse:
    out: ConnectAppAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "appAuthorizationSummary" in data:
        import aws_sdk_appfabric.types.app_authorization_summary

        out["app_authorization_summary"] = (
            aws_sdk_appfabric.types.app_authorization_summary.deserialize_json(
                data["appAuthorizationSummary"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectAppAuthorizationResponse.app_authorization_summary required"
        )
    return out

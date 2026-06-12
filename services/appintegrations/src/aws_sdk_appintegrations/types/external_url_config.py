"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExternalUrlConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_approved_origins
    import aws_sdk_appintegrations.types.url


class ExternalUrlConfig(TypedDict):
    access_url: "aws_sdk_appintegrations.types.url.URL"
    """<p>The URL to access the application.</p>"""
    approved_origins: NotRequired[
        "aws_sdk_appintegrations.types.application_approved_origins.ApplicationApprovedOrigins"
    ]
    """<p>Additional URLs to allow list if different than the access URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalUrlConfig) -> dict:
    out: dict = {}
    out["AccessUrl"] = value["access_url"]
    if "approved_origins" in value:
        import aws_sdk_appintegrations.types.application_approved_origins

        out["ApprovedOrigins"] = (
            aws_sdk_appintegrations.types.application_approved_origins.serialize_json(
                value["approved_origins"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalUrlConfig:
    out: ExternalUrlConfig = {}  # type: ignore[typeddict-item]
    if "AccessUrl" in data:
        out["access_url"] = data["AccessUrl"]
    else:
        raise DeserializationError("ExternalUrlConfig.access_url required")
    if "ApprovedOrigins" in data:
        import aws_sdk_appintegrations.types.application_approved_origins

        out["approved_origins"] = (
            aws_sdk_appintegrations.types.application_approved_origins.deserialize_json(
                data["ApprovedOrigins"]
            )
        )
    return out

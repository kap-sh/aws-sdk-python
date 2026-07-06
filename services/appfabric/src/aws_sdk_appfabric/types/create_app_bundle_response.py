"""Generated from Smithy shape ``com.amazonaws.appfabric#CreateAppBundleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_bundle


class CreateAppBundleResponse(TypedDict, closed=True):
    app_bundle: "aws_sdk_appfabric.types.app_bundle.AppBundle"
    """<p>Contains information about an app bundle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppBundleResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.app_bundle

    out["appBundle"] = aws_sdk_appfabric.types.app_bundle.serialize_json(
        value["app_bundle"]
    )
    return out


def deserialize_json(data: dict) -> CreateAppBundleResponse:
    out: CreateAppBundleResponse = {}  # type: ignore[typeddict-item]
    if "appBundle" in data:
        import aws_sdk_appfabric.types.app_bundle

        out["app_bundle"] = aws_sdk_appfabric.types.app_bundle.deserialize_json(
            data["appBundle"]
        )
    else:
        raise DeserializationError("CreateAppBundleResponse.app_bundle required")
    return out

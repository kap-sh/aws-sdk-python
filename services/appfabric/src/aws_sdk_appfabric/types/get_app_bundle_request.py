"""Generated from Smithy shape ``com.amazonaws.appfabric#GetAppBundleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier


class GetAppBundleRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppBundleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAppBundleRequest:
    out: GetAppBundleRequest = {}  # type: ignore[typeddict-item]
    return out

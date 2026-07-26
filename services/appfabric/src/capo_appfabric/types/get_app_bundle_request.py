"""Generated from Smithy shape ``com.amazonaws.appfabric#GetAppBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.identifier


class GetAppBundleRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppBundleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAppBundleRequest:
    out: GetAppBundleRequest = {}  # type: ignore[typeddict-item]
    return out

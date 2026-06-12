"""Generated from Smithy shape ``com.amazonaws.appfabric#DeleteAppBundleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier


class DeleteAppBundleRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The ID or Amazon Resource Name (ARN) of the app bundle that needs to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppBundleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppBundleRequest:
    out: DeleteAppBundleRequest = {}  # type: ignore[typeddict-item]
    return out

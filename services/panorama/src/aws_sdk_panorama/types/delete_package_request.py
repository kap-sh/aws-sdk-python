"""Generated from Smithy shape ``com.amazonaws.panorama#DeletePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.boolean
    import aws_sdk_panorama.types.node_package_id


class DeletePackageRequest(TypedDict, closed=True):
    package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId"
    """<p>The package's ID.</p>"""
    force_delete: "aws_sdk_panorama.types.boolean.Boolean"
    """<p>Delete the package even if it has artifacts stored in its access point. Deletes the package's artifacts from Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageRequest:
    out: DeletePackageRequest = {}  # type: ignore[typeddict-item]
    return out

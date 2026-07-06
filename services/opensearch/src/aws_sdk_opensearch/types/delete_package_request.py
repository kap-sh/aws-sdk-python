"""Generated from Smithy shape ``com.amazonaws.opensearch#DeletePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_id


class DeletePackageRequest(TypedDict, closed=True):
    package_id: "aws_sdk_opensearch.types.package_id.PackageID"
    """<p>The internal ID of the package you want to delete. Use <code>DescribePackages</code> to find this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageRequest:
    out: DeletePackageRequest = {}  # type: ignore[typeddict-item]
    return out

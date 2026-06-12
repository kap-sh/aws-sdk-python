"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeletePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.package_id


class DeletePackageRequest(TypedDict):
    package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID"
    """<p>Internal ID of the package that you want to delete. Use <code>DescribePackages</code> to find this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageRequest:
    out: DeletePackageRequest = {}  # type: ignore[typeddict-item]
    return out

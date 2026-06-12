"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_package_id


class DescribePackageRequest(TypedDict):
    package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId"
    """<p>The package's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePackageRequest:
    out: DescribePackageRequest = {}  # type: ignore[typeddict-item]
    return out

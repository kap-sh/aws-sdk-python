"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_details

PackageDetailsList: TypeAlias = list[
    "aws_sdk_opensearch.types.package_details.PackageDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetailsList) -> list:
    import aws_sdk_opensearch.types.package_details

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.package_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageDetailsList:
    import aws_sdk_opensearch.types.package_details

    out: PackageDetailsList = []
    for item in data:
        out.append(aws_sdk_opensearch.types.package_details.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.panorama#PackageImportJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.package_import_job

PackageImportJobList: TypeAlias = list[
    "aws_sdk_panorama.types.package_import_job.PackageImportJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageImportJobList) -> list:
    import aws_sdk_panorama.types.package_import_job

    out: list = []
    for item in value:
        out.append(aws_sdk_panorama.types.package_import_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageImportJobList:
    import aws_sdk_panorama.types.package_import_job

    out: PackageImportJobList = []
    for item in data:
        out.append(aws_sdk_panorama.types.package_import_job.deserialize_json(item))
    return out

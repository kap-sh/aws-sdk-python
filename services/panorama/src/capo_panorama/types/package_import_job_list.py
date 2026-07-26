"""Generated from Smithy shape ``com.amazonaws.panorama#PackageImportJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.package_import_job

PackageImportJobList: TypeAlias = list[
    "capo_panorama.types.package_import_job.PackageImportJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageImportJobList) -> list:
    import capo_panorama.types.package_import_job

    out: list = []
    for item in value:
        out.append(capo_panorama.types.package_import_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageImportJobList:
    import capo_panorama.types.package_import_job

    out: PackageImportJobList = []
    for item in data:
        out.append(capo_panorama.types.package_import_job.deserialize_json(item))
    return out

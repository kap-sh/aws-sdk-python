"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningRepositoryFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.scanning_repository_filter

ScanningRepositoryFilterList: TypeAlias = list[
    "capo_ecr.types.scanning_repository_filter.ScanningRepositoryFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanningRepositoryFilterList) -> list:
    import capo_ecr.types.scanning_repository_filter

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.scanning_repository_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScanningRepositoryFilterList:
    import capo_ecr.types.scanning_repository_filter

    out: ScanningRepositoryFilterList = []
    for item in data:
        out.append(
            capo_ecr.types.scanning_repository_filter.deserialize_aws_json_1_1(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningRepositoryFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.scanning_repository_filter_type
    import aws_sdk_ecr.types.scanning_repository_filter_value


class ScanningRepositoryFilter(TypedDict):
    filter: "aws_sdk_ecr.types.scanning_repository_filter_value.ScanningRepositoryFilterValue"
    """<p>The filter to use when scanning.</p>"""
    filter_type: (
        "aws_sdk_ecr.types.scanning_repository_filter_type.ScanningRepositoryFilterType"
    )
    """<p>The type associated with the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanningRepositoryFilter) -> dict:
    out: dict = {}
    out["filter"] = value["filter"]
    import aws_sdk_ecr.types.scanning_repository_filter_type

    out["filterType"] = (
        aws_sdk_ecr.types.scanning_repository_filter_type.serialize_aws_json_1_1(
            value["filter_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScanningRepositoryFilter:
    out: ScanningRepositoryFilter = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        out["filter"] = data["filter"]
    else:
        raise DeserializationError("ScanningRepositoryFilter.filter required")
    if "filterType" in data:
        import aws_sdk_ecr.types.scanning_repository_filter_type

        out["filter_type"] = (
            aws_sdk_ecr.types.scanning_repository_filter_type.deserialize_aws_json_1_1(
                data["filterType"]
            )
        )
    else:
        raise DeserializationError("ScanningRepositoryFilter.filter_type required")
    return out

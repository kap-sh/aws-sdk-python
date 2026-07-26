"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningRepositoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.scanning_repository_filter_type
    import capo_ecr.types.scanning_repository_filter_value


class ScanningRepositoryFilter(TypedDict, closed=True):
    filter: (
        "capo_ecr.types.scanning_repository_filter_value.ScanningRepositoryFilterValue"
    )
    """<p>The filter to use when scanning.</p>"""
    filter_type: (
        "capo_ecr.types.scanning_repository_filter_type.ScanningRepositoryFilterType"
    )
    """<p>The type associated with the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanningRepositoryFilter) -> dict:
    out: dict = {}
    out["filter"] = value["filter"]
    import capo_ecr.types.scanning_repository_filter_type

    out["filterType"] = (
        capo_ecr.types.scanning_repository_filter_type.serialize_aws_json_1_1(
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
        import capo_ecr.types.scanning_repository_filter_type

        out["filter_type"] = (
            capo_ecr.types.scanning_repository_filter_type.deserialize_aws_json_1_1(
                data["filterType"]
            )
        )
    else:
        raise DeserializationError("ScanningRepositoryFilter.filter_type required")
    return out

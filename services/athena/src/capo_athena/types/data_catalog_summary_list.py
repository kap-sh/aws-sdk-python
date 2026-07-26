"""Generated from Smithy shape ``com.amazonaws.athena#DataCatalogSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.data_catalog_summary

DataCatalogSummaryList: TypeAlias = list[
    "capo_athena.types.data_catalog_summary.DataCatalogSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCatalogSummaryList) -> list:
    import capo_athena.types.data_catalog_summary

    out: list = []
    for item in value:
        out.append(capo_athena.types.data_catalog_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataCatalogSummaryList:
    import capo_athena.types.data_catalog_summary

    out: DataCatalogSummaryList = []
    for item in data:
        out.append(
            capo_athena.types.data_catalog_summary.deserialize_aws_json_1_1(item)
        )
    return out

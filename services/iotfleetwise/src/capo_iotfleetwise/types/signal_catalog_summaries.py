"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#signalCatalogSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.signal_catalog_summary

signalCatalogSummaries: TypeAlias = list[
    "capo_iotfleetwise.types.signal_catalog_summary.SignalCatalogSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: signalCatalogSummaries) -> list:
    import capo_iotfleetwise.types.signal_catalog_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.signal_catalog_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> signalCatalogSummaries:
    import capo_iotfleetwise.types.signal_catalog_summary

    out: signalCatalogSummaries = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.signal_catalog_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#signalCatalogSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.signal_catalog_summary

signalCatalogSummaries: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.signal_catalog_summary.SignalCatalogSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: signalCatalogSummaries) -> list:
    import aws_sdk_iotfleetwise.types.signal_catalog_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.signal_catalog_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> signalCatalogSummaries:
    import aws_sdk_iotfleetwise.types.signal_catalog_summary

    out: signalCatalogSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.signal_catalog_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

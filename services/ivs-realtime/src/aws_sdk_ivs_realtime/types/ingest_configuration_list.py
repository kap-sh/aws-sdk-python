"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#IngestConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.ingest_configuration_summary

IngestConfigurationList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.ingest_configuration_summary.IngestConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfigurationList) -> list:
    import aws_sdk_ivs_realtime.types.ingest_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.ingest_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IngestConfigurationList:
    import aws_sdk_ivs_realtime.types.ingest_configuration_summary

    out: IngestConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.ingest_configuration_summary.deserialize_json(
                item
            )
        )
    return out

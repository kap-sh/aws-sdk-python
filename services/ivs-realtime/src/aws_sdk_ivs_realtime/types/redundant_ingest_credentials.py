"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#RedundantIngestCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.redundant_ingest_credential

RedundantIngestCredentials: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.redundant_ingest_credential.RedundantIngestCredential"
]


# --- restJson1 ser/de ---
def serialize_json(value: RedundantIngestCredentials) -> list:
    import aws_sdk_ivs_realtime.types.redundant_ingest_credential

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.redundant_ingest_credential.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RedundantIngestCredentials:
    import aws_sdk_ivs_realtime.types.redundant_ingest_credential

    out: RedundantIngestCredentials = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.redundant_ingest_credential.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#decoderManifestSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.decoder_manifest_summary

decoderManifestSummaries: TypeAlias = list[
    "capo_iotfleetwise.types.decoder_manifest_summary.DecoderManifestSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: decoderManifestSummaries) -> list:
    import capo_iotfleetwise.types.decoder_manifest_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.decoder_manifest_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> decoderManifestSummaries:
    import capo_iotfleetwise.types.decoder_manifest_summary

    out: decoderManifestSummaries = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.decoder_manifest_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

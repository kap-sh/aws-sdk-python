"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#modelManifestSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.model_manifest_summary

modelManifestSummaries: TypeAlias = list[
    "capo_iotfleetwise.types.model_manifest_summary.ModelManifestSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: modelManifestSummaries) -> list:
    import capo_iotfleetwise.types.model_manifest_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.model_manifest_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> modelManifestSummaries:
    import capo_iotfleetwise.types.model_manifest_summary

    out: modelManifestSummaries = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.model_manifest_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out

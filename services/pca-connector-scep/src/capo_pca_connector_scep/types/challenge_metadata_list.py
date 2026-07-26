"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ChallengeMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.challenge_metadata_summary

ChallengeMetadataList: TypeAlias = list[
    "capo_pca_connector_scep.types.challenge_metadata_summary.ChallengeMetadataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChallengeMetadataList) -> list:
    import capo_pca_connector_scep.types.challenge_metadata_summary

    out: list = []
    for item in value:
        out.append(
            capo_pca_connector_scep.types.challenge_metadata_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChallengeMetadataList:
    import capo_pca_connector_scep.types.challenge_metadata_summary

    out: ChallengeMetadataList = []
    for item in data:
        out.append(
            capo_pca_connector_scep.types.challenge_metadata_summary.deserialize_json(
                item
            )
        )
    return out

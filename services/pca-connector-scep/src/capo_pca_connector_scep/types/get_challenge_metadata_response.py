"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetChallengeMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.challenge_metadata


class GetChallengeMetadataResponse(TypedDict, closed=True):
    challenge_metadata: NotRequired[
        "capo_pca_connector_scep.types.challenge_metadata.ChallengeMetadata"
    ]
    """<p>The metadata for the challenge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChallengeMetadataResponse) -> dict:
    out: dict = {}
    if "challenge_metadata" in value:
        import capo_pca_connector_scep.types.challenge_metadata

        out["ChallengeMetadata"] = (
            capo_pca_connector_scep.types.challenge_metadata.serialize_json(
                value["challenge_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChallengeMetadataResponse:
    out: GetChallengeMetadataResponse = {}  # type: ignore[typeddict-item]
    if "ChallengeMetadata" in data:
        import capo_pca_connector_scep.types.challenge_metadata

        out["challenge_metadata"] = (
            capo_pca_connector_scep.types.challenge_metadata.deserialize_json(
                data["ChallengeMetadata"]
            )
        )
    return out

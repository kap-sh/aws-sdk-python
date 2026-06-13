"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#CreateChallengeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.challenge


class CreateChallengeResponse(TypedDict):
    challenge: NotRequired["aws_sdk_pca_connector_scep.types.challenge.Challenge"]
    """<p>Returns the challenge details for the specified connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChallengeResponse) -> dict:
    out: dict = {}
    if "challenge" in value:
        import aws_sdk_pca_connector_scep.types.challenge

        out["Challenge"] = aws_sdk_pca_connector_scep.types.challenge.serialize_json(
            value["challenge"]
        )
    return out


def deserialize_json(data: dict) -> CreateChallengeResponse:
    out: CreateChallengeResponse = {}  # type: ignore[typeddict-item]
    if "Challenge" in data:
        import aws_sdk_pca_connector_scep.types.challenge

        out["challenge"] = aws_sdk_pca_connector_scep.types.challenge.deserialize_json(
            data["Challenge"]
        )
    return out

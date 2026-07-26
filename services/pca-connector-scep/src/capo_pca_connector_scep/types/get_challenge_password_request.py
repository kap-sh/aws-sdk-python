"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetChallengePasswordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.challenge_arn


class GetChallengePasswordRequest(TypedDict, closed=True):
    challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn"
    """<p>The Amazon Resource Name (ARN) of the challenge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChallengePasswordRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChallengePasswordRequest:
    out: GetChallengePasswordRequest = {}  # type: ignore[typeddict-item]
    return out

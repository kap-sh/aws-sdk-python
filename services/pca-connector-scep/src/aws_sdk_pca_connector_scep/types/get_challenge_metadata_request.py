"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetChallengeMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.challenge_arn


class GetChallengeMetadataRequest(TypedDict):
    challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn"
    """<p>The Amazon Resource Name (ARN) of the challenge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChallengeMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChallengeMetadataRequest:
    out: GetChallengeMetadataRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#DeleteChallengeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.challenge_arn


class DeleteChallengeRequest(TypedDict):
    challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn"
    """<p>The Amazon Resource Name (ARN) of the challenge password to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChallengeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChallengeRequest:
    out: DeleteChallengeRequest = {}  # type: ignore[typeddict-item]
    return out

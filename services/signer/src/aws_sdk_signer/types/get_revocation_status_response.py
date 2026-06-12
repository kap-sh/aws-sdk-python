"""Generated from Smithy shape ``com.amazonaws.signer#GetRevocationStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.revoked_entities


class GetRevocationStatusResponse(TypedDict):
    revoked_entities: NotRequired[
        "aws_sdk_signer.types.revoked_entities.RevokedEntities"
    ]
    """<p>A list of revoked entities (including zero or more of the signing profile ARN, signing job ARN, and certificate hashes) supplied as input to the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRevocationStatusResponse) -> dict:
    out: dict = {}
    if "revoked_entities" in value:
        import aws_sdk_signer.types.revoked_entities

        out["revokedEntities"] = aws_sdk_signer.types.revoked_entities.serialize_json(
            value["revoked_entities"]
        )
    return out


def deserialize_json(data: dict) -> GetRevocationStatusResponse:
    out: GetRevocationStatusResponse = {}  # type: ignore[typeddict-item]
    if "revokedEntities" in data:
        import aws_sdk_signer.types.revoked_entities

        out["revoked_entities"] = (
            aws_sdk_signer.types.revoked_entities.deserialize_json(
                data["revokedEntities"]
            )
        )
    return out

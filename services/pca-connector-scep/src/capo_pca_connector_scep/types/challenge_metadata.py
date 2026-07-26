"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ChallengeMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_scep.types.challenge_arn
    import capo_pca_connector_scep.types.connector_arn


class ChallengeMetadata(TypedDict, closed=True):
    arn: NotRequired["capo_pca_connector_scep.types.challenge_arn.ChallengeArn"]
    """<p>The Amazon Resource Name (ARN) of the challenge.</p>"""
    connector_arn: NotRequired[
        "capo_pca_connector_scep.types.connector_arn.ConnectorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChallengeMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "created_at" in value:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChallengeMetadata:
    out: ChallengeMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "CreatedAt" in data:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["created_at"] = (
            capo_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import capo_pca_connector_scep.types._prelude.timestamp

        out["updated_at"] = (
            capo_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out

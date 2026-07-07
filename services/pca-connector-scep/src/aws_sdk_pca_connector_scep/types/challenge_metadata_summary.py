"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ChallengeMetadataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pca_connector_scep.types.challenge_arn
    import aws_sdk_pca_connector_scep.types.connector_arn


class ChallengeMetadataSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn"]
    """<p>The Amazon Resource Name (ARN) of the challenge.</p>"""
    connector_arn: NotRequired[
        "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the challenge was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the challenge was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChallengeMetadataSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "created_at" in value:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["UpdatedAt"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChallengeMetadataSummary:
    out: ChallengeMetadataSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "CreatedAt" in data:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_pca_connector_scep.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_pca_connector_scep.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out

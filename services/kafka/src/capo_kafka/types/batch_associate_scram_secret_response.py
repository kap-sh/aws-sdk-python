"""Generated from Smithy shape ``com.amazonaws.kafka#BatchAssociateScramSecretResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_unprocessed_scram_secret
    import capo_kafka.types.__string


class BatchAssociateScramSecretResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    unprocessed_scram_secrets: NotRequired[
        "capo_kafka.types.__list_of_unprocessed_scram_secret.__listOfUnprocessedScramSecret"
    ]
    """<p>List of errors when associating secrets to cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateScramSecretResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "unprocessed_scram_secrets" in value:
        import capo_kafka.types.__list_of_unprocessed_scram_secret

        out["unprocessedScramSecrets"] = (
            capo_kafka.types.__list_of_unprocessed_scram_secret.serialize_json(
                value["unprocessed_scram_secrets"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateScramSecretResponse:
    out: BatchAssociateScramSecretResponse = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "unprocessedScramSecrets" in data:
        import capo_kafka.types.__list_of_unprocessed_scram_secret

        out["unprocessed_scram_secrets"] = (
            capo_kafka.types.__list_of_unprocessed_scram_secret.deserialize_json(
                data["unprocessedScramSecrets"]
            )
        )
    return out

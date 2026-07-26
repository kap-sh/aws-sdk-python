"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfUnprocessedScramSecret``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.unprocessed_scram_secret

__listOfUnprocessedScramSecret: TypeAlias = list[
    "capo_kafka.types.unprocessed_scram_secret.UnprocessedScramSecret"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUnprocessedScramSecret) -> list:
    import capo_kafka.types.unprocessed_scram_secret

    out: list = []
    for item in value:
        out.append(capo_kafka.types.unprocessed_scram_secret.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUnprocessedScramSecret:
    import capo_kafka.types.unprocessed_scram_secret

    out: __listOfUnprocessedScramSecret = []
    for item in data:
        out.append(capo_kafka.types.unprocessed_scram_secret.deserialize_json(item))
    return out

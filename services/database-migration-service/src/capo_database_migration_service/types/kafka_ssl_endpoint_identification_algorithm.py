"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSslEndpointIdentificationAlgorithm``."""

from typing import Literal, TypeAlias, cast

KafkaSslEndpointIdentificationAlgorithm: TypeAlias = Literal[
    "none",
    "https",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KafkaSslEndpointIdentificationAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KafkaSslEndpointIdentificationAlgorithm:
    return cast(KafkaSslEndpointIdentificationAlgorithm, data)

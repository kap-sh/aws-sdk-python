"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetSchemaType``."""

from typing import Literal, TypeAlias, cast

"""<p> Versioned schema type for dataset examples. Each value identifies both the source format and the version of that format's schema. </p>"""
DatasetSchemaType: TypeAlias = Literal[
    "AGENTCORE_EVALUATION_PREDEFINED_V1",
    "AGENTCORE_EVALUATION_SIMULATED_V1",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSchemaType) -> str:
    return value


def deserialize_json(data: str) -> DatasetSchemaType:
    return cast(DatasetSchemaType, data)

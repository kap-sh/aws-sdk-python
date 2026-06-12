"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityFailures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.capability_failure

CapabilityFailures: TypeAlias = list[
    "aws_sdk_opensearch.types.capability_failure.CapabilityFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityFailures) -> list:
    import aws_sdk_opensearch.types.capability_failure

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.capability_failure.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapabilityFailures:
    import aws_sdk_opensearch.types.capability_failure

    out: CapabilityFailures = []
    for item in data:
        out.append(aws_sdk_opensearch.types.capability_failure.deserialize_json(item))
    return out

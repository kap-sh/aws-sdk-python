"""Generated from Smithy shape ``com.amazonaws.opensearch#ValidationFailures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.validation_failure

ValidationFailures: TypeAlias = list[
    "aws_sdk_opensearch.types.validation_failure.ValidationFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationFailures) -> list:
    import aws_sdk_opensearch.types.validation_failure

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.validation_failure.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationFailures:
    import aws_sdk_opensearch.types.validation_failure

    out: ValidationFailures = []
    for item in data:
        out.append(aws_sdk_opensearch.types.validation_failure.deserialize_json(item))
    return out

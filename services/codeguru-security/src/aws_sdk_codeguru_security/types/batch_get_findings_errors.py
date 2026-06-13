"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#BatchGetFindingsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.batch_get_findings_error

BatchGetFindingsErrors: TypeAlias = list[
    "aws_sdk_codeguru_security.types.batch_get_findings_error.BatchGetFindingsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsErrors) -> list:
    import aws_sdk_codeguru_security.types.batch_get_findings_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_security.types.batch_get_findings_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetFindingsErrors:
    import aws_sdk_codeguru_security.types.batch_get_findings_error

    out: BatchGetFindingsErrors = []
    for item in data:
        out.append(
            aws_sdk_codeguru_security.types.batch_get_findings_error.deserialize_json(
                item
            )
        )
    return out

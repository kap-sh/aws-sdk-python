"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfJobScopeTerm``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.job_scope_term

__listOfJobScopeTerm: TypeAlias = list[
    "aws_sdk_macie2.types.job_scope_term.JobScopeTerm"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJobScopeTerm) -> list:
    import aws_sdk_macie2.types.job_scope_term

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.job_scope_term.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJobScopeTerm:
    import aws_sdk_macie2.types.job_scope_term

    out: __listOfJobScopeTerm = []
    for item in data:
        out.append(aws_sdk_macie2.types.job_scope_term.deserialize_json(item))
    return out

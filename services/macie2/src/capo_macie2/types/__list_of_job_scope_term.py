"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfJobScopeTerm``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.job_scope_term

__listOfJobScopeTerm: TypeAlias = list["capo_macie2.types.job_scope_term.JobScopeTerm"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJobScopeTerm) -> list:
    import capo_macie2.types.job_scope_term

    out: list = []
    for item in value:
        out.append(capo_macie2.types.job_scope_term.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJobScopeTerm:
    import capo_macie2.types.job_scope_term

    out: __listOfJobScopeTerm = []
    for item in data:
        out.append(capo_macie2.types.job_scope_term.deserialize_json(item))
    return out

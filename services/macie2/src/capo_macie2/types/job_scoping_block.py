"""Generated from Smithy shape ``com.amazonaws.macie2#JobScopingBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_job_scope_term

JobScopingBlock = TypedDict(
    "JobScopingBlock",
    {
        "and": NotRequired[
            "capo_macie2.types.__list_of_job_scope_term.__listOfJobScopeTerm"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: JobScopingBlock) -> dict:
    out: dict = {}
    if "and" in value:
        import capo_macie2.types.__list_of_job_scope_term

        out["and"] = capo_macie2.types.__list_of_job_scope_term.serialize_json(
            value["and"]
        )
    return out


def deserialize_json(data: dict) -> JobScopingBlock:
    out: JobScopingBlock = {}  # type: ignore[typeddict-item]
    if "and" in data:
        import capo_macie2.types.__list_of_job_scope_term

        out["and"] = capo_macie2.types.__list_of_job_scope_term.deserialize_json(
            data["and"]
        )
    return out

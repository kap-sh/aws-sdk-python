"""Generated from Smithy shape ``com.amazonaws.macie2#JobScopingBlock``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_job_scope_term

JobScopingBlock = TypedDict(
    "JobScopingBlock",
    {
        "and": NotRequired[
            "aws_sdk_macie2.types.__list_of_job_scope_term.__listOfJobScopeTerm"
        ],
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: JobScopingBlock) -> dict:
    out: dict = {}
    if "and" in value:
        import aws_sdk_macie2.types.__list_of_job_scope_term

        out["and"] = aws_sdk_macie2.types.__list_of_job_scope_term.serialize_json(
            value["and"]
        )
    return out


def deserialize_json(data: dict) -> JobScopingBlock:
    out: JobScopingBlock = {}  # type: ignore[typeddict-item]
    if "and" in data:
        import aws_sdk_macie2.types.__list_of_job_scope_term

        out["and"] = aws_sdk_macie2.types.__list_of_job_scope_term.deserialize_json(
            data["and"]
        )
    return out

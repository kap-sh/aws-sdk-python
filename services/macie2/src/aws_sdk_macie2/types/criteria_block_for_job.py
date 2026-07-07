"""Generated from Smithy shape ``com.amazonaws.macie2#CriteriaBlockForJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_criteria_for_job

CriteriaBlockForJob = TypedDict(
    "CriteriaBlockForJob",
    {
        "and": NotRequired[
            "aws_sdk_macie2.types.__list_of_criteria_for_job.__listOfCriteriaForJob"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: CriteriaBlockForJob) -> dict:
    out: dict = {}
    if "and" in value:
        import aws_sdk_macie2.types.__list_of_criteria_for_job

        out["and"] = aws_sdk_macie2.types.__list_of_criteria_for_job.serialize_json(
            value["and"]
        )
    return out


def deserialize_json(data: dict) -> CriteriaBlockForJob:
    out: CriteriaBlockForJob = {}  # type: ignore[typeddict-item]
    if "and" in data:
        import aws_sdk_macie2.types.__list_of_criteria_for_job

        out["and"] = aws_sdk_macie2.types.__list_of_criteria_for_job.deserialize_json(
            data["and"]
        )
    return out

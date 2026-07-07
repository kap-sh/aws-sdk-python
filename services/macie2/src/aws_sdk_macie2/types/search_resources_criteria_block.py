"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesCriteriaBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_search_resources_criteria

SearchResourcesCriteriaBlock = TypedDict(
    "SearchResourcesCriteriaBlock",
    {
        "and": NotRequired[
            "aws_sdk_macie2.types.__list_of_search_resources_criteria.__listOfSearchResourcesCriteria"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesCriteriaBlock) -> dict:
    out: dict = {}
    if "and" in value:
        import aws_sdk_macie2.types.__list_of_search_resources_criteria

        out["and"] = (
            aws_sdk_macie2.types.__list_of_search_resources_criteria.serialize_json(
                value["and"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchResourcesCriteriaBlock:
    out: SearchResourcesCriteriaBlock = {}  # type: ignore[typeddict-item]
    if "and" in data:
        import aws_sdk_macie2.types.__list_of_search_resources_criteria

        out["and"] = (
            aws_sdk_macie2.types.__list_of_search_resources_criteria.deserialize_json(
                data["and"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.test_case_search_criteria

TestCaseSearchConditionList: TypeAlias = list[
    "capo_connect.types.test_case_search_criteria.TestCaseSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseSearchConditionList) -> list:
    import capo_connect.types.test_case_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.test_case_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestCaseSearchConditionList:
    import capo_connect.types.test_case_search_criteria

    out: TestCaseSearchConditionList = []
    for item in data:
        out.append(capo_connect.types.test_case_search_criteria.deserialize_json(item))
    return out

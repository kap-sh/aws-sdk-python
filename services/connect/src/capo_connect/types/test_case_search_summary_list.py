"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.test_case

TestCaseSearchSummaryList: TypeAlias = list["capo_connect.types.test_case.TestCase"]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseSearchSummaryList) -> list:
    import capo_connect.types.test_case

    out: list = []
    for item in value:
        out.append(capo_connect.types.test_case.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestCaseSearchSummaryList:
    import capo_connect.types.test_case

    out: TestCaseSearchSummaryList = []
    for item in data:
        out.append(capo_connect.types.test_case.deserialize_json(item))
    return out

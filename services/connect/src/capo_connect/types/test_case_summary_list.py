"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.test_case_summary

TestCaseSummaryList: TypeAlias = list[
    "capo_connect.types.test_case_summary.TestCaseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseSummaryList) -> list:
    import capo_connect.types.test_case_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.test_case_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestCaseSummaryList:
    import capo_connect.types.test_case_summary

    out: TestCaseSummaryList = []
    for item in data:
        out.append(capo_connect.types.test_case_summary.deserialize_json(item))
    return out

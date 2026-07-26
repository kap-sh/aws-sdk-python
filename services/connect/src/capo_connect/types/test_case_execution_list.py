"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.test_case_execution

TestCaseExecutionList: TypeAlias = list[
    "capo_connect.types.test_case_execution.TestCaseExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseExecutionList) -> list:
    import capo_connect.types.test_case_execution

    out: list = []
    for item in value:
        out.append(capo_connect.types.test_case_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestCaseExecutionList:
    import capo_connect.types.test_case_execution

    out: TestCaseExecutionList = []
    for item in data:
        out.append(capo_connect.types.test_case_execution.deserialize_json(item))
    return out

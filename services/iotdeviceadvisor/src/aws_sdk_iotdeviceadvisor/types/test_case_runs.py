"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.test_case_run

TestCaseRuns: TypeAlias = list[
    "aws_sdk_iotdeviceadvisor.types.test_case_run.TestCaseRun"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseRuns) -> list:
    import aws_sdk_iotdeviceadvisor.types.test_case_run

    out: list = []
    for item in value:
        out.append(aws_sdk_iotdeviceadvisor.types.test_case_run.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestCaseRuns:
    import aws_sdk_iotdeviceadvisor.types.test_case_run

    out: TestCaseRuns = []
    for item in data:
        out.append(aws_sdk_iotdeviceadvisor.types.test_case_run.deserialize_json(item))
    return out

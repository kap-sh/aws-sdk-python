"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.group_name
    import aws_sdk_iotdeviceadvisor.types.test_case_runs
    import aws_sdk_iotdeviceadvisor.types.uuid


class GroupResult(TypedDict):
    group_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Group result ID.</p>"""
    group_name: NotRequired["aws_sdk_iotdeviceadvisor.types.group_name.GroupName"]
    """<p>Group Result Name.</p>"""
    tests: NotRequired["aws_sdk_iotdeviceadvisor.types.test_case_runs.TestCaseRuns"]
    """<p>Tests under Group Result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupResult) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "tests" in value:
        import aws_sdk_iotdeviceadvisor.types.test_case_runs

        out["tests"] = aws_sdk_iotdeviceadvisor.types.test_case_runs.serialize_json(
            value["tests"]
        )
    return out


def deserialize_json(data: dict) -> GroupResult:
    out: GroupResult = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "tests" in data:
        import aws_sdk_iotdeviceadvisor.types.test_case_runs

        out["tests"] = aws_sdk_iotdeviceadvisor.types.test_case_runs.deserialize_json(
            data["tests"]
        )
    return out

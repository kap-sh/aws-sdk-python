"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.group_result_list


class TestResult(TypedDict):
    groups: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.group_result_list.GroupResultList"
    ]
    """<p>Show each group of test results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestResult) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_iotdeviceadvisor.types.group_result_list

        out["groups"] = aws_sdk_iotdeviceadvisor.types.group_result_list.serialize_json(
            value["groups"]
        )
    return out


def deserialize_json(data: dict) -> TestResult:
    out: TestResult = {}  # type: ignore[typeddict-item]
    if "groups" in data:
        import aws_sdk_iotdeviceadvisor.types.group_result_list

        out["groups"] = (
            aws_sdk_iotdeviceadvisor.types.group_result_list.deserialize_json(
                data["groups"]
            )
        )
    return out

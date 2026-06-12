"""Generated from Smithy shape ``com.amazonaws.devicefarm#ScheduleRunResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.run


class ScheduleRunResult(TypedDict):
    run: NotRequired["aws_sdk_device_farm.types.run.Run"]
    """<p>Information about the scheduled run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleRunResult) -> dict:
    out: dict = {}
    if "run" in value:
        import aws_sdk_device_farm.types.run

        out["run"] = aws_sdk_device_farm.types.run.serialize_aws_json_1_1(value["run"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleRunResult:
    out: ScheduleRunResult = {}  # type: ignore[typeddict-item]
    if "run" in data:
        import aws_sdk_device_farm.types.run

        out["run"] = aws_sdk_device_farm.types.run.deserialize_aws_json_1_1(data["run"])
    return out

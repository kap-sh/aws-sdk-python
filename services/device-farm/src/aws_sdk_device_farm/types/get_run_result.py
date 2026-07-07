"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetRunResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.run


class GetRunResult(TypedDict, closed=True):
    run: NotRequired["aws_sdk_device_farm.types.run.Run"]
    """<p>The run to get results from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRunResult) -> dict:
    out: dict = {}
    if "run" in value:
        import aws_sdk_device_farm.types.run

        out["run"] = aws_sdk_device_farm.types.run.serialize_aws_json_1_1(value["run"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRunResult:
    out: GetRunResult = {}  # type: ignore[typeddict-item]
    if "run" in data:
        import aws_sdk_device_farm.types.run

        out["run"] = aws_sdk_device_farm.types.run.deserialize_aws_json_1_1(data["run"])
    return out

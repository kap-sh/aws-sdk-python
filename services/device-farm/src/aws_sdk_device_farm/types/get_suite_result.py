"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetSuiteResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.suite


class GetSuiteResult(TypedDict):
    suite: NotRequired["aws_sdk_device_farm.types.suite.Suite"]
    """<p>A collection of one or more tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSuiteResult) -> dict:
    out: dict = {}
    if "suite" in value:
        import aws_sdk_device_farm.types.suite

        out["suite"] = aws_sdk_device_farm.types.suite.serialize_aws_json_1_1(
            value["suite"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSuiteResult:
    out: GetSuiteResult = {}  # type: ignore[typeddict-item]
    if "suite" in data:
        import aws_sdk_device_farm.types.suite

        out["suite"] = aws_sdk_device_farm.types.suite.deserialize_aws_json_1_1(
            data["suite"]
        )
    return out

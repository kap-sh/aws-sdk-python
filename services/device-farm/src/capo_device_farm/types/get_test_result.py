"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetTestResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.test


class GetTestResult(TypedDict, closed=True):
    test: NotRequired["capo_device_farm.types.test.Test"]
    """<p>A test condition that is evaluated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTestResult) -> dict:
    out: dict = {}
    if "test" in value:
        import capo_device_farm.types.test

        out["test"] = capo_device_farm.types.test.serialize_aws_json_1_1(value["test"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTestResult:
    out: GetTestResult = {}  # type: ignore[typeddict-item]
    if "test" in data:
        import capo_device_farm.types.test

        out["test"] = capo_device_farm.types.test.deserialize_aws_json_1_1(data["test"])
    return out

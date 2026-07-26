"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetSuiteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.suite


class GetSuiteResult(TypedDict, closed=True):
    suite: NotRequired["capo_device_farm.types.suite.Suite"]
    """<p>A collection of one or more tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSuiteResult) -> dict:
    out: dict = {}
    if "suite" in value:
        import capo_device_farm.types.suite

        out["suite"] = capo_device_farm.types.suite.serialize_aws_json_1_1(
            value["suite"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSuiteResult:
    out: GetSuiteResult = {}  # type: ignore[typeddict-item]
    if "suite" in data:
        import capo_device_farm.types.suite

        out["suite"] = capo_device_farm.types.suite.deserialize_aws_json_1_1(
            data["suite"]
        )
    return out

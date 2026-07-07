"""Generated from Smithy shape ``com.amazonaws.devicefarm#UniqueProblem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.problems


class UniqueProblem(TypedDict, closed=True):
    message: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>A message about the unique problems' result.</p>"""
    problems: NotRequired["aws_sdk_device_farm.types.problems.Problems"]
    """<p>Information about the problems.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UniqueProblem) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "problems" in value:
        import aws_sdk_device_farm.types.problems

        out["problems"] = aws_sdk_device_farm.types.problems.serialize_aws_json_1_1(
            value["problems"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UniqueProblem:
    out: UniqueProblem = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "problems" in data:
        import aws_sdk_device_farm.types.problems

        out["problems"] = aws_sdk_device_farm.types.problems.deserialize_aws_json_1_1(
            data["problems"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.devicefarm#Problem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device
    import aws_sdk_device_farm.types.execution_result
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.problem_detail


class Problem(TypedDict):
    run: NotRequired["aws_sdk_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated run.</p>"""
    job: NotRequired["aws_sdk_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated job.</p>"""
    suite: NotRequired["aws_sdk_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated suite.</p>"""
    test: NotRequired["aws_sdk_device_farm.types.problem_detail.ProblemDetail"]
    """<p>Information about the associated test.</p>"""
    device: NotRequired["aws_sdk_device_farm.types.device.Device"]
    """<p>Information about the associated device.</p>"""
    result: NotRequired["aws_sdk_device_farm.types.execution_result.ExecutionResult"]
    """<p>The problem's result.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PASSED</p> </li> <li> <p>WARNED</p> </li> <li> <p>FAILED</p> </li> <li> <p>SKIPPED</p> </li> <li> <p>ERRORED</p> </li> <li> <p>STOPPED</p> </li> </ul>"""
    message: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>A message about the problem's result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Problem) -> dict:
    out: dict = {}
    if "run" in value:
        import aws_sdk_device_farm.types.problem_detail

        out["run"] = aws_sdk_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["run"]
        )
    if "job" in value:
        import aws_sdk_device_farm.types.problem_detail

        out["job"] = aws_sdk_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["job"]
        )
    if "suite" in value:
        import aws_sdk_device_farm.types.problem_detail

        out["suite"] = aws_sdk_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["suite"]
        )
    if "test" in value:
        import aws_sdk_device_farm.types.problem_detail

        out["test"] = aws_sdk_device_farm.types.problem_detail.serialize_aws_json_1_1(
            value["test"]
        )
    if "device" in value:
        import aws_sdk_device_farm.types.device

        out["device"] = aws_sdk_device_farm.types.device.serialize_aws_json_1_1(
            value["device"]
        )
    if "result" in value:
        import aws_sdk_device_farm.types.execution_result

        out["result"] = (
            aws_sdk_device_farm.types.execution_result.serialize_aws_json_1_1(
                value["result"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Problem:
    out: Problem = {}  # type: ignore[typeddict-item]
    if "run" in data:
        import aws_sdk_device_farm.types.problem_detail

        out["run"] = aws_sdk_device_farm.types.problem_detail.deserialize_aws_json_1_1(
            data["run"]
        )
    if "job" in data:
        import aws_sdk_device_farm.types.problem_detail

        out["job"] = aws_sdk_device_farm.types.problem_detail.deserialize_aws_json_1_1(
            data["job"]
        )
    if "suite" in data:
        import aws_sdk_device_farm.types.problem_detail

        out["suite"] = (
            aws_sdk_device_farm.types.problem_detail.deserialize_aws_json_1_1(
                data["suite"]
            )
        )
    if "test" in data:
        import aws_sdk_device_farm.types.problem_detail

        out["test"] = aws_sdk_device_farm.types.problem_detail.deserialize_aws_json_1_1(
            data["test"]
        )
    if "device" in data:
        import aws_sdk_device_farm.types.device

        out["device"] = aws_sdk_device_farm.types.device.deserialize_aws_json_1_1(
            data["device"]
        )
    if "result" in data:
        import aws_sdk_device_farm.types.execution_result

        out["result"] = (
            aws_sdk_device_farm.types.execution_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out

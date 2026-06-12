"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetJobResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.job


class GetJobResult(TypedDict):
    job: NotRequired["aws_sdk_device_farm.types.job.Job"]
    """<p>An object that contains information about the requested job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobResult) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_device_farm.types.job

        out["job"] = aws_sdk_device_farm.types.job.serialize_aws_json_1_1(value["job"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobResult:
    out: GetJobResult = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_device_farm.types.job

        out["job"] = aws_sdk_device_farm.types.job.deserialize_aws_json_1_1(data["job"])
    return out

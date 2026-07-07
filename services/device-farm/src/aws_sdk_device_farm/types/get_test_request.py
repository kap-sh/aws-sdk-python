"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name


class GetTestRequest(TypedDict, closed=True):
    arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The test's ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTestRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTestRequest:
    out: GetTestRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetTestRequest.arn required")
    return out

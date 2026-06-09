"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DescribeDaemonRequest(TypedDict):
    daemon_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonRequest) -> dict:
    out: dict = {}
    out["daemonArn"] = value["daemon_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonRequest:
    out: DescribeDaemonRequest = {}  # type: ignore[typeddict-item]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
    else:
        raise DeserializationError("DescribeDaemonRequest.daemon_arn required")
    return out

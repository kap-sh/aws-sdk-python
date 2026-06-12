"""Generated from Smithy shape ``com.amazonaws.batch#UpdateServiceEnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class UpdateServiceEnvironmentResponse(TypedDict):
    service_environment_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the service environment that was updated.</p>"""
    service_environment_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service environment that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceEnvironmentResponse) -> dict:
    out: dict = {}
    if "service_environment_name" in value:
        out["serviceEnvironmentName"] = value["service_environment_name"]
    if "service_environment_arn" in value:
        out["serviceEnvironmentArn"] = value["service_environment_arn"]
    return out


def deserialize_json(data: dict) -> UpdateServiceEnvironmentResponse:
    out: UpdateServiceEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "serviceEnvironmentName" in data:
        out["service_environment_name"] = data["serviceEnvironmentName"]
    if "serviceEnvironmentArn" in data:
        out["service_environment_arn"] = data["serviceEnvironmentArn"]
    return out

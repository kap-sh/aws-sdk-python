"""Generated from Smithy shape ``com.amazonaws.batch#CreateServiceEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class CreateServiceEnvironmentResponse(TypedDict, closed=True):
    service_environment_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the service environment.</p>"""
    service_environment_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceEnvironmentResponse) -> dict:
    out: dict = {}
    if "service_environment_name" in value:
        out["serviceEnvironmentName"] = value["service_environment_name"]
    if "service_environment_arn" in value:
        out["serviceEnvironmentArn"] = value["service_environment_arn"]
    return out


def deserialize_json(data: dict) -> CreateServiceEnvironmentResponse:
    out: CreateServiceEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "serviceEnvironmentName" in data:
        out["service_environment_name"] = data["serviceEnvironmentName"]
    if "serviceEnvironmentArn" in data:
        out["service_environment_arn"] = data["serviceEnvironmentArn"]
    return out

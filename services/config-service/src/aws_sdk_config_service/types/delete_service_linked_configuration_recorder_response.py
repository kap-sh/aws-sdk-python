"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteServiceLinkedConfigurationRecorderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.recorder_name


class DeleteServiceLinkedConfigurationRecorderResponse(TypedDict, closed=True):
    arn: "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>"""
    name: "aws_sdk_config_service.types.recorder_name.RecorderName"
    """<p>The name of the specified configuration recorder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteServiceLinkedConfigurationRecorderResponse,
) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteServiceLinkedConfigurationRecorderResponse:
    out: DeleteServiceLinkedConfigurationRecorderResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "DeleteServiceLinkedConfigurationRecorderResponse.arn required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "DeleteServiceLinkedConfigurationRecorderResponse.name required"
        )
    return out

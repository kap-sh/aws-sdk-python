"""Generated from Smithy shape ``com.amazonaws.configservice#PutServiceLinkedConfigurationRecorderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.recorder_name


class PutServiceLinkedConfigurationRecorderResponse(TypedDict):
    arn: NotRequired[
        "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>"""
    name: NotRequired["aws_sdk_config_service.types.recorder_name.RecorderName"]
    r"""<p>The name of the specified configuration recorder.</p> <p>For service-linked configuration recorders, Config automatically assigns a name that has the prefix \"<code>AWSConfigurationRecorderFor</code>\" to the new service-linked configuration recorder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PutServiceLinkedConfigurationRecorderResponse,
) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutServiceLinkedConfigurationRecorderResponse:
    out: PutServiceLinkedConfigurationRecorderResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out

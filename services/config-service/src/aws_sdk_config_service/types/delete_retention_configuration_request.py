"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteRetentionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.retention_configuration_name


class DeleteRetentionConfigurationRequest(TypedDict):
    retention_configuration_name: "aws_sdk_config_service.types.retention_configuration_name.RetentionConfigurationName"
    """<p>The name of the retention configuration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRetentionConfigurationRequest) -> dict:
    out: dict = {}
    out["RetentionConfigurationName"] = value["retention_configuration_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRetentionConfigurationRequest:
    out: DeleteRetentionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "RetentionConfigurationName" in data:
        out["retention_configuration_name"] = data["RetentionConfigurationName"]
    else:
        raise DeserializationError(
            "DeleteRetentionConfigurationRequest.retention_configuration_name required"
        )
    return out

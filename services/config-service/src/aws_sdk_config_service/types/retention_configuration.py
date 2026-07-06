"""Generated from Smithy shape ``com.amazonaws.configservice#RetentionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.retention_configuration_name
    import aws_sdk_config_service.types.retention_period_in_days


class RetentionConfiguration(TypedDict, closed=True):
    name: "aws_sdk_config_service.types.retention_configuration_name.RetentionConfigurationName"
    """<p>The name of the retention configuration object.</p>"""
    retention_period_in_days: (
        "aws_sdk_config_service.types.retention_period_in_days.RetentionPeriodInDays"
    )
    """<p>Number of days Config stores your historical information.</p> <note> <p>Currently, only applicable to the configuration item history.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetentionConfiguration:
    out: RetentionConfiguration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RetentionConfiguration.name required")
    if "RetentionPeriodInDays" in data:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    else:
        raise DeserializationError(
            "RetentionConfiguration.retention_period_in_days required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationRecorderStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder_status_list


class DescribeConfigurationRecorderStatusResponse(TypedDict):
    configuration_recorders_status: NotRequired[
        "aws_sdk_config_service.types.configuration_recorder_status_list.ConfigurationRecorderStatusList"
    ]
    """<p>A list that contains status of the specified recorders.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationRecorderStatusResponse) -> dict:
    out: dict = {}
    if "configuration_recorders_status" in value:
        import aws_sdk_config_service.types.configuration_recorder_status_list

        out["ConfigurationRecordersStatus"] = (
            aws_sdk_config_service.types.configuration_recorder_status_list.serialize_aws_json_1_1(
                value["configuration_recorders_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationRecorderStatusResponse:
    out: DescribeConfigurationRecorderStatusResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecordersStatus" in data:
        import aws_sdk_config_service.types.configuration_recorder_status_list

        out["configuration_recorders_status"] = (
            aws_sdk_config_service.types.configuration_recorder_status_list.deserialize_aws_json_1_1(
                data["ConfigurationRecordersStatus"]
            )
        )
    return out

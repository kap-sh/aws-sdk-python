"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationRecorderStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration_recorder_status_list


class DescribeConfigurationRecorderStatusResponse(TypedDict, closed=True):
    configuration_recorders_status: NotRequired[
        "capo_config_service.types.configuration_recorder_status_list.ConfigurationRecorderStatusList"
    ]
    """<p>A list that contains status of the specified recorders.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationRecorderStatusResponse) -> dict:
    out: dict = {}
    if "configuration_recorders_status" in value:
        import capo_config_service.types.configuration_recorder_status_list

        out["ConfigurationRecordersStatus"] = (
            capo_config_service.types.configuration_recorder_status_list.serialize_aws_json_1_1(
                value["configuration_recorders_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationRecorderStatusResponse:
    out: DescribeConfigurationRecorderStatusResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecordersStatus" in data:
        import capo_config_service.types.configuration_recorder_status_list

        out["configuration_recorders_status"] = (
            capo_config_service.types.configuration_recorder_status_list.deserialize_aws_json_1_1(
                data["ConfigurationRecordersStatus"]
            )
        )
    return out

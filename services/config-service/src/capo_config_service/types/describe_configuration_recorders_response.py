"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationRecordersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration_recorder_list


class DescribeConfigurationRecordersResponse(TypedDict, closed=True):
    configuration_recorders: NotRequired[
        "capo_config_service.types.configuration_recorder_list.ConfigurationRecorderList"
    ]
    """<p>A list that contains the descriptions of the specified configuration recorders.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationRecordersResponse) -> dict:
    out: dict = {}
    if "configuration_recorders" in value:
        import capo_config_service.types.configuration_recorder_list

        out["ConfigurationRecorders"] = (
            capo_config_service.types.configuration_recorder_list.serialize_aws_json_1_1(
                value["configuration_recorders"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationRecordersResponse:
    out: DescribeConfigurationRecordersResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorders" in data:
        import capo_config_service.types.configuration_recorder_list

        out["configuration_recorders"] = (
            capo_config_service.types.configuration_recorder_list.deserialize_aws_json_1_1(
                data["ConfigurationRecorders"]
            )
        )
    return out

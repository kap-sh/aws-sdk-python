"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder_filter_name
    import aws_sdk_config_service.types.configuration_recorder_filter_values


class ConfigurationRecorderFilter(TypedDict):
    filter_name: NotRequired[
        "aws_sdk_config_service.types.configuration_recorder_filter_name.ConfigurationRecorderFilterName"
    ]
    """<p>The name of the type of filter. Currently, only <code>recordingScope</code> is supported.</p>"""
    filter_value: NotRequired[
        "aws_sdk_config_service.types.configuration_recorder_filter_values.ConfigurationRecorderFilterValues"
    ]
    """<p>The value of the filter. For <code>recordingScope</code>, valid values include: <code>INTERNAL</code> and <code>PAID</code>.</p> <p> <code>INTERNAL</code> indicates that the <a href=\"https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html\">ConfigurationItems</a> in scope for the configuration recorder are recorded for free.</p> <p> <code>PAID</code> indicates that the <a href=\"https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html\">ConfigurationItems</a> in scope for the configuration recorder impact the costs to your bill.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderFilter) -> dict:
    out: dict = {}
    if "filter_name" in value:
        import aws_sdk_config_service.types.configuration_recorder_filter_name

        out["filterName"] = (
            aws_sdk_config_service.types.configuration_recorder_filter_name.serialize_aws_json_1_1(
                value["filter_name"]
            )
        )
    if "filter_value" in value:
        import aws_sdk_config_service.types.configuration_recorder_filter_values

        out["filterValue"] = (
            aws_sdk_config_service.types.configuration_recorder_filter_values.serialize_aws_json_1_1(
                value["filter_value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationRecorderFilter:
    out: ConfigurationRecorderFilter = {}  # type: ignore[typeddict-item]
    if "filterName" in data:
        import aws_sdk_config_service.types.configuration_recorder_filter_name

        out["filter_name"] = (
            aws_sdk_config_service.types.configuration_recorder_filter_name.deserialize_aws_json_1_1(
                data["filterName"]
            )
        )
    if "filterValue" in data:
        import aws_sdk_config_service.types.configuration_recorder_filter_values

        out["filter_value"] = (
            aws_sdk_config_service.types.configuration_recorder_filter_values.deserialize_aws_json_1_1(
                data["filterValue"]
            )
        )
    return out

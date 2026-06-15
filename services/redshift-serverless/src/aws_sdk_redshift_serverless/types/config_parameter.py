"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ConfigParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.parameter_key
    import aws_sdk_redshift_serverless.types.parameter_value


class ConfigParameter(TypedDict):
    parameter_key: NotRequired[
        "aws_sdk_redshift_serverless.types.parameter_key.ParameterKey"
    ]
    r"""<p>The key of the parameter. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. For more information about query monitoring rules and available metrics, see <a href=\"https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless\">Query monitoring metrics for Amazon Redshift Serverless</a>.</p>"""
    parameter_value: NotRequired[
        "aws_sdk_redshift_serverless.types.parameter_value.ParameterValue"
    ]
    """<p>The value of the parameter to set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigParameter) -> dict:
    out: dict = {}
    if "parameter_key" in value:
        out["parameterKey"] = value["parameter_key"]
    if "parameter_value" in value:
        out["parameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigParameter:
    out: ConfigParameter = {}  # type: ignore[typeddict-item]
    if "parameterKey" in data:
        out["parameter_key"] = data["parameterKey"]
    if "parameterValue" in data:
        out["parameter_value"] = data["parameterValue"]
    return out

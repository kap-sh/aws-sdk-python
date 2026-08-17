"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderLoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.log_group
    import capo_lambda.types.system_log_level


class CapacityProviderLoggingConfig(TypedDict, closed=True):
    system_log_level: NotRequired["capo_lambda.types.system_log_level.SystemLogLevel"]
    """<p>Set this property to filter the system logs for your capacity provider that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where <code>DEBUG</code> is the highest level and <code>WARN</code> is the lowest.</p>"""
    log_group: NotRequired["capo_lambda.types.log_group.LogGroup"]
    """<p>The name of the Amazon CloudWatch log group the capacity provider sends logs to. By default, Lambda capacity providers send logs to a default log group named <code>/aws/lambda/capacity-provider/&lt;capacity provider name&gt;</code>. To use a different log group, enter an existing log group or enter a new log group name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderLoggingConfig) -> dict:
    out: dict = {}
    if "system_log_level" in value:
        import capo_lambda.types.system_log_level

        out["SystemLogLevel"] = capo_lambda.types.system_log_level.serialize_json(
            value["system_log_level"]
        )
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    return out


def deserialize_json(data: dict) -> CapacityProviderLoggingConfig:
    out: CapacityProviderLoggingConfig = {}  # type: ignore[typeddict-item]
    if data.get("SystemLogLevel") is not None:
        import capo_lambda.types.system_log_level

        out["system_log_level"] = capo_lambda.types.system_log_level.deserialize_json(
            data["SystemLogLevel"]
        )
    if data.get("LogGroup") is not None:
        out["log_group"] = data["LogGroup"]
    return out

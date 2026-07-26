"""Generated from Smithy shape ``com.amazonaws.configservice#SsmControls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.percentage


class SsmControls(TypedDict, closed=True):
    concurrent_execution_rate_percentage: NotRequired[
        "capo_config_service.types.percentage.Percentage"
    ]
    """<p>The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10. </p>"""
    error_percentage: NotRequired["capo_config_service.types.percentage.Percentage"]
    """<p>The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SsmControls) -> dict:
    out: dict = {}
    if "concurrent_execution_rate_percentage" in value:
        out["ConcurrentExecutionRatePercentage"] = value[
            "concurrent_execution_rate_percentage"
        ]
    if "error_percentage" in value:
        out["ErrorPercentage"] = value["error_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SsmControls:
    out: SsmControls = {}  # type: ignore[typeddict-item]
    if "ConcurrentExecutionRatePercentage" in data:
        out["concurrent_execution_rate_percentage"] = data[
            "ConcurrentExecutionRatePercentage"
        ]
    if "ErrorPercentage" in data:
        out["error_percentage"] = data["ErrorPercentage"]
    return out

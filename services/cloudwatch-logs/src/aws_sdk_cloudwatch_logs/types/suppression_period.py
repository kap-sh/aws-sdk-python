"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SuppressionPeriod``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.integer
    import aws_sdk_cloudwatch_logs.types.suppression_unit


class SuppressionPeriod(TypedDict):
    value: "aws_sdk_cloudwatch_logs.types.integer.Integer"
    """<p>Specifies the number of seconds, minutes or hours to suppress this anomaly. There is no maximum.</p>"""
    suppression_unit: NotRequired[
        "aws_sdk_cloudwatch_logs.types.suppression_unit.SuppressionUnit"
    ]
    """<p>Specifies whether the value of <code>value</code> is in seconds, minutes, or hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuppressionPeriod) -> dict:
    out: dict = {}
    out["value"] = value.get("value", 0)
    if "suppression_unit" in value:
        import aws_sdk_cloudwatch_logs.types.suppression_unit

        out["suppressionUnit"] = (
            aws_sdk_cloudwatch_logs.types.suppression_unit.serialize_aws_json_1_1(
                value["suppression_unit"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuppressionPeriod:
    out: SuppressionPeriod = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    if "suppressionUnit" in data:
        import aws_sdk_cloudwatch_logs.types.suppression_unit

        out["suppression_unit"] = (
            aws_sdk_cloudwatch_logs.types.suppression_unit.deserialize_aws_json_1_1(
                data["suppressionUnit"]
            )
        )
    return out

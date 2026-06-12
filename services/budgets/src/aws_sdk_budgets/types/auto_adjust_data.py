"""Generated from Smithy shape ``com.amazonaws.budgets#AutoAdjustData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.auto_adjust_type
    import aws_sdk_budgets.types.generic_timestamp
    import aws_sdk_budgets.types.historical_options


class AutoAdjustData(TypedDict):
    auto_adjust_type: "aws_sdk_budgets.types.auto_adjust_type.AutoAdjustType"
    """<p>The string that defines whether your budget auto-adjusts based on historical or forecasted data.</p>"""
    historical_options: NotRequired[
        "aws_sdk_budgets.types.historical_options.HistoricalOptions"
    ]
    """<p>The parameters that define or describe the historical data that your auto-adjusting budget is based on.</p>"""
    last_auto_adjust_time: NotRequired[
        "aws_sdk_budgets.types.generic_timestamp.GenericTimestamp"
    ]
    """<p>The last time that your budget was auto-adjusted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoAdjustData) -> dict:
    out: dict = {}
    import aws_sdk_budgets.types.auto_adjust_type

    out["AutoAdjustType"] = (
        aws_sdk_budgets.types.auto_adjust_type.serialize_aws_json_1_1(
            value["auto_adjust_type"]
        )
    )
    if "historical_options" in value:
        import aws_sdk_budgets.types.historical_options

        out["HistoricalOptions"] = (
            aws_sdk_budgets.types.historical_options.serialize_aws_json_1_1(
                value["historical_options"]
            )
        )
    if "last_auto_adjust_time" in value:
        import aws_sdk_budgets.types.generic_timestamp

        out["LastAutoAdjustTime"] = (
            aws_sdk_budgets.types.generic_timestamp.serialize_aws_json_1_1(
                value["last_auto_adjust_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoAdjustData:
    out: AutoAdjustData = {}  # type: ignore[typeddict-item]
    if "AutoAdjustType" in data:
        import aws_sdk_budgets.types.auto_adjust_type

        out["auto_adjust_type"] = (
            aws_sdk_budgets.types.auto_adjust_type.deserialize_aws_json_1_1(
                data["AutoAdjustType"]
            )
        )
    else:
        raise DeserializationError("AutoAdjustData.auto_adjust_type required")
    if "HistoricalOptions" in data:
        import aws_sdk_budgets.types.historical_options

        out["historical_options"] = (
            aws_sdk_budgets.types.historical_options.deserialize_aws_json_1_1(
                data["HistoricalOptions"]
            )
        )
    if "LastAutoAdjustTime" in data:
        import aws_sdk_budgets.types.generic_timestamp

        out["last_auto_adjust_time"] = (
            aws_sdk_budgets.types.generic_timestamp.deserialize_aws_json_1_1(
                data["LastAutoAdjustTime"]
            )
        )
    return out

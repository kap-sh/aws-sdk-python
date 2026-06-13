"""Generated from Smithy shape ``com.amazonaws.braket#SpendingLimitSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.spending_limit_arn
    import aws_sdk_braket.types.tags_map
    import aws_sdk_braket.types.time_period


class SpendingLimitSummary(TypedDict):
    spending_limit_arn: "aws_sdk_braket.types.spending_limit_arn.SpendingLimitArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the spending limit.</p>"""
    device_arn: "aws_sdk_braket.types.device_arn.DeviceArn"
    """<p>The Amazon Resource Name (ARN) of the quantum device associated with this spending limit.</p>"""
    time_period: "aws_sdk_braket.types.time_period.TimePeriod"
    """<p>The time period during which the spending limit is active.</p>"""
    spending_limit: "str"
    """<p>The maximum spending amount allowed for the device during the specified time period, in USD.</p>"""
    queued_spend: "str"
    """<p>The amount currently queued for spending on the device, in USD.</p>"""
    total_spend: "str"
    """<p>The total amount spent on the device so far during the current time period, in USD.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the spending limit was created, in epoch seconds.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the spending limit was last modified, in epoch seconds.</p>"""
    tags: NotRequired["aws_sdk_braket.types.tags_map.TagsMap"]
    """<p>The tags associated with the spending limit. Each tag consists of a key and an optional value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpendingLimitSummary) -> dict:
    out: dict = {}
    out["spendingLimitArn"] = value["spending_limit_arn"]
    out["deviceArn"] = value["device_arn"]
    import aws_sdk_braket.types.time_period

    out["timePeriod"] = aws_sdk_braket.types.time_period.serialize_json(
        value["time_period"]
    )
    out["spendingLimit"] = value["spending_limit"]
    out["queuedSpend"] = value["queued_spend"]
    out["totalSpend"] = value["total_spend"]
    import aws_sdk_braket.types._prelude.timestamp

    out["createdAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_braket.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "tags" in value:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SpendingLimitSummary:
    out: SpendingLimitSummary = {}  # type: ignore[typeddict-item]
    if "spendingLimitArn" in data:
        out["spending_limit_arn"] = data["spendingLimitArn"]
    else:
        raise DeserializationError("SpendingLimitSummary.spending_limit_arn required")
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("SpendingLimitSummary.device_arn required")
    if "timePeriod" in data:
        import aws_sdk_braket.types.time_period

        out["time_period"] = aws_sdk_braket.types.time_period.deserialize_json(
            data["timePeriod"]
        )
    else:
        raise DeserializationError("SpendingLimitSummary.time_period required")
    if "spendingLimit" in data:
        out["spending_limit"] = data["spendingLimit"]
    else:
        raise DeserializationError("SpendingLimitSummary.spending_limit required")
    if "queuedSpend" in data:
        out["queued_spend"] = data["queuedSpend"]
    else:
        raise DeserializationError("SpendingLimitSummary.queued_spend required")
    if "totalSpend" in data:
        out["total_spend"] = data["totalSpend"]
    else:
        raise DeserializationError("SpendingLimitSummary.total_spend required")
    if "createdAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["created_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("SpendingLimitSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["updated_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("SpendingLimitSummary.updated_at required")
    if "tags" in data:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.deserialize_json(data["tags"])
    return out

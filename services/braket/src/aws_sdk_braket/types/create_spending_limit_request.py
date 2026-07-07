"""Generated from Smithy shape ``com.amazonaws.braket#CreateSpendingLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.tags_map
    import aws_sdk_braket.types.time_period


class CreateSpendingLimitRequest(TypedDict, closed=True):
    client_token: "aws_sdk_braket.types.string64.String64"
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>"""
    device_arn: "aws_sdk_braket.types.device_arn.DeviceArn"
    """<p>The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.</p>"""
    spending_limit: "str"
    """<p>The maximum amount that can be spent on the specified device, in USD.</p>"""
    time_period: NotRequired["aws_sdk_braket.types.time_period.TimePeriod"]
    """<p>The time period during which the spending limit is active, including start and end dates.</p>"""
    tags: NotRequired["aws_sdk_braket.types.tags_map.TagsMap"]
    """<p>The tags to apply to the spending limit. Each tag consists of a key and an optional value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSpendingLimitRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["deviceArn"] = value["device_arn"]
    out["spendingLimit"] = value["spending_limit"]
    if "time_period" in value:
        import aws_sdk_braket.types.time_period

        out["timePeriod"] = aws_sdk_braket.types.time_period.serialize_json(
            value["time_period"]
        )
    if "tags" in value:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSpendingLimitRequest:
    out: CreateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateSpendingLimitRequest.client_token required")
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("CreateSpendingLimitRequest.device_arn required")
    if "spendingLimit" in data:
        out["spending_limit"] = data["spendingLimit"]
    else:
        raise DeserializationError("CreateSpendingLimitRequest.spending_limit required")
    if "timePeriod" in data:
        import aws_sdk_braket.types.time_period

        out["time_period"] = aws_sdk_braket.types.time_period.deserialize_json(
            data["timePeriod"]
        )
    if "tags" in data:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.deserialize_json(data["tags"])
    return out

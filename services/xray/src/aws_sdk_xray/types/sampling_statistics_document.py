"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStatisticsDocument``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.borrow_count
    import aws_sdk_xray.types.client_id
    import aws_sdk_xray.types.request_count
    import aws_sdk_xray.types.rule_name
    import aws_sdk_xray.types.sampled_count
    import aws_sdk_xray.types.timestamp


class SamplingStatisticsDocument(TypedDict):
    rule_name: "aws_sdk_xray.types.rule_name.RuleName"
    """<p>The name of the sampling rule.</p>"""
    client_id: "aws_sdk_xray.types.client_id.ClientID"
    """<p>A unique identifier for the service in hexadecimal.</p>"""
    timestamp: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The current time.</p>"""
    request_count: "aws_sdk_xray.types.request_count.RequestCount"
    """<p>The number of requests that matched the rule.</p>"""
    sampled_count: "aws_sdk_xray.types.sampled_count.SampledCount"
    """<p>The number of requests recorded.</p>"""
    borrow_count: "aws_sdk_xray.types.borrow_count.BorrowCount"
    """<p>The number of requests recorded with borrowed reservoir quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStatisticsDocument) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    out["ClientID"] = value["client_id"]
    import aws_sdk_xray.types.timestamp

    out["Timestamp"] = aws_sdk_xray.types.timestamp.serialize_json(value["timestamp"])
    out["RequestCount"] = value.get("request_count", 0)
    out["SampledCount"] = value.get("sampled_count", 0)
    out["BorrowCount"] = value.get("borrow_count", 0)
    return out


def deserialize_json(data: dict) -> SamplingStatisticsDocument:
    out: SamplingStatisticsDocument = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError("SamplingStatisticsDocument.rule_name required")
    if "ClientID" in data:
        out["client_id"] = data["ClientID"]
    else:
        raise DeserializationError("SamplingStatisticsDocument.client_id required")
    if "Timestamp" in data:
        import aws_sdk_xray.types.timestamp

        out["timestamp"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    else:
        raise DeserializationError("SamplingStatisticsDocument.timestamp required")
    if "RequestCount" in data:
        out["request_count"] = data["RequestCount"]
    else:
        out["request_count"] = 0
    if "SampledCount" in data:
        out["sampled_count"] = data["SampledCount"]
    else:
        out["sampled_count"] = 0
    if "BorrowCount" in data:
        out["borrow_count"] = data["BorrowCount"]
    else:
        out["borrow_count"] = 0
    return out

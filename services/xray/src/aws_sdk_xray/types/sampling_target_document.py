"""Generated from Smithy shape ``com.amazonaws.xray#SamplingTargetDocument``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.double
    import aws_sdk_xray.types.nullable_integer
    import aws_sdk_xray.types.sampling_boost
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.timestamp


class SamplingTargetDocument(TypedDict):
    rule_name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The name of the sampling rule.</p>"""
    fixed_rate: "aws_sdk_xray.types.double.Double"
    """<p>The percentage of matching requests to instrument, after the reservoir is exhausted.</p>"""
    reservoir_quota: NotRequired["aws_sdk_xray.types.nullable_integer.NullableInteger"]
    """<p>The number of requests per second that X-Ray allocated for this service.</p>"""
    reservoir_quota_ttl: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>When the reservoir quota expires.</p>"""
    interval: NotRequired["aws_sdk_xray.types.nullable_integer.NullableInteger"]
    """<p>The number of seconds for the service to wait before getting sampling targets again.</p>"""
    sampling_boost: NotRequired["aws_sdk_xray.types.sampling_boost.SamplingBoost"]
    """<p>The sampling boost that X-Ray allocated for this service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingTargetDocument) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    out["FixedRate"] = value.get("fixed_rate", 0)
    if "reservoir_quota" in value:
        out["ReservoirQuota"] = value["reservoir_quota"]
    if "reservoir_quota_ttl" in value:
        import aws_sdk_xray.types.timestamp

        out["ReservoirQuotaTTL"] = aws_sdk_xray.types.timestamp.serialize_json(
            value["reservoir_quota_ttl"]
        )
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "sampling_boost" in value:
        import aws_sdk_xray.types.sampling_boost

        out["SamplingBoost"] = aws_sdk_xray.types.sampling_boost.serialize_json(
            value["sampling_boost"]
        )
    return out


def deserialize_json(data: dict) -> SamplingTargetDocument:
    out: SamplingTargetDocument = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "FixedRate" in data:
        out["fixed_rate"] = data["FixedRate"]
    else:
        out["fixed_rate"] = 0
    if "ReservoirQuota" in data:
        out["reservoir_quota"] = data["ReservoirQuota"]
    if "ReservoirQuotaTTL" in data:
        import aws_sdk_xray.types.timestamp

        out["reservoir_quota_ttl"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["ReservoirQuotaTTL"]
        )
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "SamplingBoost" in data:
        import aws_sdk_xray.types.sampling_boost

        out["sampling_boost"] = aws_sdk_xray.types.sampling_boost.deserialize_json(
            data["SamplingBoost"]
        )
    return out

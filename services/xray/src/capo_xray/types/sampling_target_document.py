"""Generated from Smithy shape ``com.amazonaws.xray#SamplingTargetDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.double
    import capo_xray.types.nullable_integer
    import capo_xray.types.sampling_boost
    import capo_xray.types.string
    import capo_xray.types.timestamp


class SamplingTargetDocument(TypedDict, closed=True):
    rule_name: NotRequired["capo_xray.types.string.String"]
    """<p>The name of the sampling rule.</p>"""
    fixed_rate: "capo_xray.types.double.Double"
    """<p>The percentage of matching requests to instrument, after the reservoir is exhausted.</p>"""
    reservoir_quota: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>The number of requests per second that X-Ray allocated for this service.</p>"""
    reservoir_quota_ttl: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>When the reservoir quota expires.</p>"""
    interval: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>The number of seconds for the service to wait before getting sampling targets again.</p>"""
    sampling_boost: NotRequired["capo_xray.types.sampling_boost.SamplingBoost"]
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
        import capo_xray.types.timestamp

        out["ReservoirQuotaTTL"] = capo_xray.types.timestamp.serialize_json(
            value["reservoir_quota_ttl"]
        )
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "sampling_boost" in value:
        import capo_xray.types.sampling_boost

        out["SamplingBoost"] = capo_xray.types.sampling_boost.serialize_json(
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
        import capo_xray.types.timestamp

        out["reservoir_quota_ttl"] = capo_xray.types.timestamp.deserialize_json(
            data["ReservoirQuotaTTL"]
        )
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "SamplingBoost" in data:
        import capo_xray.types.sampling_boost

        out["sampling_boost"] = capo_xray.types.sampling_boost.deserialize_json(
            data["SamplingBoost"]
        )
    return out

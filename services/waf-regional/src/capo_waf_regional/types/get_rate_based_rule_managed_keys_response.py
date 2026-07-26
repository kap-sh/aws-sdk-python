"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRateBasedRuleManagedKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.managed_keys
    import capo_waf_regional.types.next_marker


class GetRateBasedRuleManagedKeysResponse(TypedDict, closed=True):
    managed_keys: NotRequired["capo_waf_regional.types.managed_keys.ManagedKeys"]
    """<p>An array of IP addresses that currently are blocked by the specified <a>RateBasedRule</a>. </p>"""
    next_marker: NotRequired["capo_waf_regional.types.next_marker.NextMarker"]
    """<p>A null value and not currently used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedRuleManagedKeysResponse) -> dict:
    out: dict = {}
    if "managed_keys" in value:
        import capo_waf_regional.types.managed_keys

        out["ManagedKeys"] = (
            capo_waf_regional.types.managed_keys.serialize_aws_json_1_1(
                value["managed_keys"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedRuleManagedKeysResponse:
    out: GetRateBasedRuleManagedKeysResponse = {}  # type: ignore[typeddict-item]
    if "ManagedKeys" in data:
        import capo_waf_regional.types.managed_keys

        out["managed_keys"] = (
            capo_waf_regional.types.managed_keys.deserialize_aws_json_1_1(
                data["ManagedKeys"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out

"""Generated from Smithy shape ``com.amazonaws.waf#GetRateBasedRuleManagedKeysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.managed_keys
    import aws_sdk_waf.types.next_marker


class GetRateBasedRuleManagedKeysResponse(TypedDict):
    managed_keys: NotRequired["aws_sdk_waf.types.managed_keys.ManagedKeys"]
    """<p>An array of IP addresses that currently are blocked by the specified <a>RateBasedRule</a>. </p>"""
    next_marker: NotRequired["aws_sdk_waf.types.next_marker.NextMarker"]
    """<p>A null value and not currently used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedRuleManagedKeysResponse) -> dict:
    out: dict = {}
    if "managed_keys" in value:
        import aws_sdk_waf.types.managed_keys

        out["ManagedKeys"] = aws_sdk_waf.types.managed_keys.serialize_aws_json_1_1(
            value["managed_keys"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedRuleManagedKeysResponse:
    out: GetRateBasedRuleManagedKeysResponse = {}  # type: ignore[typeddict-item]
    if "ManagedKeys" in data:
        import aws_sdk_waf.types.managed_keys

        out["managed_keys"] = aws_sdk_waf.types.managed_keys.deserialize_aws_json_1_1(
            data["ManagedKeys"]
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out

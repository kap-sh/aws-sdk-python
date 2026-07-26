"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRateBasedStatementManagedKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.rate_based_statement_managed_keys_ip_set


class GetRateBasedStatementManagedKeysResponse(TypedDict, closed=True):
    managed_keys_ipv4: NotRequired[
        "capo_wafv2.types.rate_based_statement_managed_keys_ip_set.RateBasedStatementManagedKeysIPSet"
    ]
    """<p>The keys that are of Internet Protocol version 4 (IPv4). </p>"""
    managed_keys_ipv6: NotRequired[
        "capo_wafv2.types.rate_based_statement_managed_keys_ip_set.RateBasedStatementManagedKeysIPSet"
    ]
    """<p>The keys that are of Internet Protocol version 6 (IPv6). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedStatementManagedKeysResponse) -> dict:
    out: dict = {}
    if "managed_keys_ipv4" in value:
        import capo_wafv2.types.rate_based_statement_managed_keys_ip_set

        out["ManagedKeysIPV4"] = (
            capo_wafv2.types.rate_based_statement_managed_keys_ip_set.serialize_aws_json_1_1(
                value["managed_keys_ipv4"]
            )
        )
    if "managed_keys_ipv6" in value:
        import capo_wafv2.types.rate_based_statement_managed_keys_ip_set

        out["ManagedKeysIPV6"] = (
            capo_wafv2.types.rate_based_statement_managed_keys_ip_set.serialize_aws_json_1_1(
                value["managed_keys_ipv6"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedStatementManagedKeysResponse:
    out: GetRateBasedStatementManagedKeysResponse = {}  # type: ignore[typeddict-item]
    if "ManagedKeysIPV4" in data:
        import capo_wafv2.types.rate_based_statement_managed_keys_ip_set

        out["managed_keys_ipv4"] = (
            capo_wafv2.types.rate_based_statement_managed_keys_ip_set.deserialize_aws_json_1_1(
                data["ManagedKeysIPV4"]
            )
        )
    if "ManagedKeysIPV6" in data:
        import capo_wafv2.types.rate_based_statement_managed_keys_ip_set

        out["managed_keys_ipv6"] = (
            capo_wafv2.types.rate_based_statement_managed_keys_ip_set.deserialize_aws_json_1_1(
                data["ManagedKeysIPV6"]
            )
        )
    return out

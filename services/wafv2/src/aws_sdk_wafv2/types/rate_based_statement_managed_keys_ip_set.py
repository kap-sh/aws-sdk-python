"""Generated from Smithy shape ``com.amazonaws.wafv2#RateBasedStatementManagedKeysIPSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.ip_address_version
    import aws_sdk_wafv2.types.ip_addresses


class RateBasedStatementManagedKeysIPSet(TypedDict, closed=True):
    ip_address_version: NotRequired[
        "aws_sdk_wafv2.types.ip_address_version.IPAddressVersion"
    ]
    """<p>The version of the IP addresses, either <code>IPV4</code> or <code>IPV6</code>. </p>"""
    addresses: NotRequired["aws_sdk_wafv2.types.ip_addresses.IPAddresses"]
    """<p>The IP addresses that are currently blocked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateBasedStatementManagedKeysIPSet) -> dict:
    out: dict = {}
    if "ip_address_version" in value:
        import aws_sdk_wafv2.types.ip_address_version

        out["IPAddressVersion"] = (
            aws_sdk_wafv2.types.ip_address_version.serialize_aws_json_1_1(
                value["ip_address_version"]
            )
        )
    if "addresses" in value:
        import aws_sdk_wafv2.types.ip_addresses

        out["Addresses"] = aws_sdk_wafv2.types.ip_addresses.serialize_aws_json_1_1(
            value["addresses"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RateBasedStatementManagedKeysIPSet:
    out: RateBasedStatementManagedKeysIPSet = {}  # type: ignore[typeddict-item]
    if "IPAddressVersion" in data:
        import aws_sdk_wafv2.types.ip_address_version

        out["ip_address_version"] = (
            aws_sdk_wafv2.types.ip_address_version.deserialize_aws_json_1_1(
                data["IPAddressVersion"]
            )
        )
    if "Addresses" in data:
        import aws_sdk_wafv2.types.ip_addresses

        out["addresses"] = aws_sdk_wafv2.types.ip_addresses.deserialize_aws_json_1_1(
            data["Addresses"]
        )
    return out

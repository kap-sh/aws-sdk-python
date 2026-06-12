"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkAccountInfoWithFingerprint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.amazon_id
    import aws_sdk_iot_wireless.types.fingerprint
    import aws_sdk_iot_wireless.types.partner_account_arn


class SidewalkAccountInfoWithFingerprint(TypedDict):
    amazon_id: NotRequired["aws_sdk_iot_wireless.types.amazon_id.AmazonId"]
    """<p>The Sidewalk Amazon ID.</p>"""
    fingerprint: NotRequired["aws_sdk_iot_wireless.types.fingerprint.Fingerprint"]
    """<p>The fingerprint of the Sidewalk application server private key.</p>"""
    arn: NotRequired["aws_sdk_iot_wireless.types.partner_account_arn.PartnerAccountArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkAccountInfoWithFingerprint) -> dict:
    out: dict = {}
    if "amazon_id" in value:
        out["AmazonId"] = value["amazon_id"]
    if "fingerprint" in value:
        out["Fingerprint"] = value["fingerprint"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SidewalkAccountInfoWithFingerprint:
    out: SidewalkAccountInfoWithFingerprint = {}  # type: ignore[typeddict-item]
    if "AmazonId" in data:
        out["amazon_id"] = data["AmazonId"]
    if "Fingerprint" in data:
        out["fingerprint"] = data["Fingerprint"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out

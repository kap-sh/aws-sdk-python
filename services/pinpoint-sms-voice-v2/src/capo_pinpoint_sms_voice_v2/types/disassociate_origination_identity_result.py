"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DisassociateOriginationIdentityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iso_country_code


class DisassociateOriginationIdentityResult(TypedDict, closed=True):
    pool_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the pool.</p>"""
    pool_id: NotRequired["str"]
    """<p>The PoolId of the pool no longer associated with the origination identity.</p>"""
    origination_identity_arn: NotRequired["str"]
    """<p>The PhoneNumberArn or SenderIdArn of the origination identity.</p>"""
    origination_identity: NotRequired["str"]
    """<p>The PhoneNumberId or SenderId of the origination identity.</p>"""
    iso_country_code: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateOriginationIdentityResult) -> dict:
    out: dict = {}
    if "pool_arn" in value:
        out["PoolArn"] = value["pool_arn"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "origination_identity_arn" in value:
        out["OriginationIdentityArn"] = value["origination_identity_arn"]
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateOriginationIdentityResult:
    out: DisassociateOriginationIdentityResult = {}  # type: ignore[typeddict-item]
    if "PoolArn" in data:
        out["pool_arn"] = data["PoolArn"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "OriginationIdentityArn" in data:
        out["origination_identity_arn"] = data["OriginationIdentityArn"]
    if "OriginationIdentity" in data:
        out["origination_identity"] = data["OriginationIdentity"]
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    return out

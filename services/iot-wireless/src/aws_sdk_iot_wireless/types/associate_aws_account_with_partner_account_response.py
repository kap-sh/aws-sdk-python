"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateAwsAccountWithPartnerAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.partner_account_arn
    import aws_sdk_iot_wireless.types.sidewalk_account_info


class AssociateAwsAccountWithPartnerAccountResponse(TypedDict):
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_account_info.SidewalkAccountInfo"
    ]
    """<p>The Sidewalk account credentials.</p>"""
    arn: NotRequired["aws_sdk_iot_wireless.types.partner_account_arn.PartnerAccountArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAwsAccountWithPartnerAccountResponse) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_account_info

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_account_info.serialize_json(
                value["sidewalk"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AssociateAwsAccountWithPartnerAccountResponse:
    out: AssociateAwsAccountWithPartnerAccountResponse = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_account_info

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_account_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out

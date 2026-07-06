"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Entitlement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_string
    import aws_sdk_mediaconnect.types.encryption
    import aws_sdk_mediaconnect.types.entitlement_status


class Entitlement(TypedDict, closed=True):
    data_transfer_subscriber_fee_percent: NotRequired["int"]
    """<p> Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</p>"""
    description: NotRequired["str"]
    """<p> A description of the entitlement.</p>"""
    encryption: NotRequired["aws_sdk_mediaconnect.types.encryption.Encryption"]
    """<p> The type of encryption that will be used on the output that is associated with this entitlement.</p>"""
    entitlement_arn: NotRequired["str"]
    """<p> The ARN of the entitlement. </p>"""
    entitlement_status: NotRequired[
        "aws_sdk_mediaconnect.types.entitlement_status.EntitlementStatus"
    ]
    """<p> An indication of whether the entitlement is enabled. </p>"""
    name: NotRequired["str"]
    """<p> The name of the entitlement. </p>"""
    subscribers: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Entitlement) -> dict:
    out: dict = {}
    if "data_transfer_subscriber_fee_percent" in value:
        out["dataTransferSubscriberFeePercent"] = value[
            "data_transfer_subscriber_fee_percent"
        ]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption" in value:
        import aws_sdk_mediaconnect.types.encryption

        out["encryption"] = aws_sdk_mediaconnect.types.encryption.serialize_json(
            value["encryption"]
        )
    if "entitlement_arn" in value:
        out["entitlementArn"] = value["entitlement_arn"]
    if "entitlement_status" in value:
        import aws_sdk_mediaconnect.types.entitlement_status

        out["entitlementStatus"] = (
            aws_sdk_mediaconnect.types.entitlement_status.serialize_json(
                value["entitlement_status"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "subscribers" in value:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["subscribers"] = aws_sdk_mediaconnect.types.__list_of_string.serialize_json(
            value["subscribers"]
        )
    return out


def deserialize_json(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
    if "dataTransferSubscriberFeePercent" in data:
        out["data_transfer_subscriber_fee_percent"] = data[
            "dataTransferSubscriberFeePercent"
        ]
    if "description" in data:
        out["description"] = data["description"]
    if "encryption" in data:
        import aws_sdk_mediaconnect.types.encryption

        out["encryption"] = aws_sdk_mediaconnect.types.encryption.deserialize_json(
            data["encryption"]
        )
    if "entitlementArn" in data:
        out["entitlement_arn"] = data["entitlementArn"]
    if "entitlementStatus" in data:
        import aws_sdk_mediaconnect.types.entitlement_status

        out["entitlement_status"] = (
            aws_sdk_mediaconnect.types.entitlement_status.deserialize_json(
                data["entitlementStatus"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "subscribers" in data:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["subscribers"] = (
            aws_sdk_mediaconnect.types.__list_of_string.deserialize_json(
                data["subscribers"]
            )
        )
    return out

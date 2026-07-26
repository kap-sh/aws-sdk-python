"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GrantEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_string
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.encryption
    import capo_mediaconnect.types.entitlement_status


class GrantEntitlementRequest(TypedDict, closed=True):
    data_transfer_subscriber_fee_percent: NotRequired["int"]
    """<p> Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</p>"""
    description: NotRequired["str"]
    """<p> A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user. </p>"""
    encryption: NotRequired["capo_mediaconnect.types.encryption.Encryption"]
    """<p> The type of encryption that will be used on the output that is associated with this entitlement. Allowable encryption types: static-key, speke.</p>"""
    entitlement_status: NotRequired[
        "capo_mediaconnect.types.entitlement_status.EntitlementStatus"
    ]
    """<p> An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.</p>"""
    name: NotRequired["str"]
    """<p> The name of the entitlement. This value must be unique within the current flow.</p>"""
    subscribers: NotRequired["capo_mediaconnect.types.__list_of_string.__listOfString"]
    """<p> The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.</p>"""
    entitlement_tags: NotRequired[
        "capo_mediaconnect.types.__map_of_string.__mapOfString"
    ]
    """<p> The key-value pairs that can be used to tag and organize the entitlement. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantEntitlementRequest) -> dict:
    out: dict = {}
    if "data_transfer_subscriber_fee_percent" in value:
        out["dataTransferSubscriberFeePercent"] = value[
            "data_transfer_subscriber_fee_percent"
        ]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption" in value:
        import capo_mediaconnect.types.encryption

        out["encryption"] = capo_mediaconnect.types.encryption.serialize_json(
            value["encryption"]
        )
    if "entitlement_status" in value:
        import capo_mediaconnect.types.entitlement_status

        out["entitlementStatus"] = (
            capo_mediaconnect.types.entitlement_status.serialize_json(
                value["entitlement_status"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "subscribers" in value:
        import capo_mediaconnect.types.__list_of_string

        out["subscribers"] = capo_mediaconnect.types.__list_of_string.serialize_json(
            value["subscribers"]
        )
    if "entitlement_tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["entitlementTags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["entitlement_tags"]
        )
    return out


def deserialize_json(data: dict) -> GrantEntitlementRequest:
    out: GrantEntitlementRequest = {}  # type: ignore[typeddict-item]
    if "dataTransferSubscriberFeePercent" in data:
        out["data_transfer_subscriber_fee_percent"] = data[
            "dataTransferSubscriberFeePercent"
        ]
    if "description" in data:
        out["description"] = data["description"]
    if "encryption" in data:
        import capo_mediaconnect.types.encryption

        out["encryption"] = capo_mediaconnect.types.encryption.deserialize_json(
            data["encryption"]
        )
    if "entitlementStatus" in data:
        import capo_mediaconnect.types.entitlement_status

        out["entitlement_status"] = (
            capo_mediaconnect.types.entitlement_status.deserialize_json(
                data["entitlementStatus"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "subscribers" in data:
        import capo_mediaconnect.types.__list_of_string

        out["subscribers"] = capo_mediaconnect.types.__list_of_string.deserialize_json(
            data["subscribers"]
        )
    if "entitlementTags" in data:
        import capo_mediaconnect.types.__map_of_string

        out["entitlement_tags"] = (
            capo_mediaconnect.types.__map_of_string.deserialize_json(
                data["entitlementTags"]
            )
        )
    return out

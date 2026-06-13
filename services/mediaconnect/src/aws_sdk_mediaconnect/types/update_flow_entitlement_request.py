"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateFlowEntitlementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_string
    import aws_sdk_mediaconnect.types.entitlement_status
    import aws_sdk_mediaconnect.types.flow_arn
    import aws_sdk_mediaconnect.types.update_encryption


class UpdateFlowEntitlementRequest(TypedDict):
    description: NotRequired["str"]
    """<p> A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.</p>"""
    encryption: NotRequired[
        "aws_sdk_mediaconnect.types.update_encryption.UpdateEncryption"
    ]
    """<p> The type of encryption that will be used on the output associated with this entitlement. Allowable encryption types: static-key, speke.</p>"""
    entitlement_arn: "str"
    """<p> The Amazon Resource Name (ARN) of the entitlement that you want to update.</p>"""
    entitlement_status: NotRequired[
        "aws_sdk_mediaconnect.types.entitlement_status.EntitlementStatus"
    ]
    """<p> An indication of whether you want to enable the entitlement to allow access, or disable it to stop streaming content to the subscriber’s flow temporarily. If you don’t specify the <code>entitlementStatus</code> field in your request, MediaConnect leaves the value unchanged.</p>"""
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The ARN of the flow that is associated with the entitlement that you want to update.</p>"""
    subscribers: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowEntitlementRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "encryption" in value:
        import aws_sdk_mediaconnect.types.update_encryption

        out["encryption"] = aws_sdk_mediaconnect.types.update_encryption.serialize_json(
            value["encryption"]
        )
    if "entitlement_status" in value:
        import aws_sdk_mediaconnect.types.entitlement_status

        out["entitlementStatus"] = (
            aws_sdk_mediaconnect.types.entitlement_status.serialize_json(
                value["entitlement_status"]
            )
        )
    if "subscribers" in value:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["subscribers"] = aws_sdk_mediaconnect.types.__list_of_string.serialize_json(
            value["subscribers"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowEntitlementRequest:
    out: UpdateFlowEntitlementRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "encryption" in data:
        import aws_sdk_mediaconnect.types.update_encryption

        out["encryption"] = (
            aws_sdk_mediaconnect.types.update_encryption.deserialize_json(
                data["encryption"]
            )
        )
    if "entitlementStatus" in data:
        import aws_sdk_mediaconnect.types.entitlement_status

        out["entitlement_status"] = (
            aws_sdk_mediaconnect.types.entitlement_status.deserialize_json(
                data["entitlementStatus"]
            )
        )
    if "subscribers" in data:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["subscribers"] = (
            aws_sdk_mediaconnect.types.__list_of_string.deserialize_json(
                data["subscribers"]
            )
        )
    return out

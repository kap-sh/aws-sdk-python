"""Generated from Smithy shape ``com.amazonaws.eks#CreateEksAnywhereSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.eks_anywhere_subscription_license_type
    import capo_eks.types.eks_anywhere_subscription_name
    import capo_eks.types.eks_anywhere_subscription_term
    import capo_eks.types.integer
    import capo_eks.types.string
    import capo_eks.types.tag_map


class CreateEksAnywhereSubscriptionRequest(TypedDict, closed=True):
    name: "capo_eks.types.eks_anywhere_subscription_name.EksAnywhereSubscriptionName"
    """<p>The unique name for your subscription. It must be unique in your Amazon Web Services account in the Amazon Web Services Region you're creating the subscription in. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphabetic character and can't be longer than 100 characters.</p>"""
    term: "capo_eks.types.eks_anywhere_subscription_term.EksAnywhereSubscriptionTerm"
    """<p>An object representing the term duration and term unit type of your subscription. This determines the term length of your subscription. Valid values are MONTHS for term unit and 12 or 36 for term duration, indicating a 12 month or 36 month subscription. This value cannot be changed after creating the subscription.</p>"""
    license_quantity: "capo_eks.types.integer.Integer"
    """<p>The number of licenses to purchase with the subscription. Valid values are between 1 and 100. This value can't be changed after creating the subscription.</p>"""
    license_type: NotRequired[
        "capo_eks.types.eks_anywhere_subscription_license_type.EksAnywhereSubscriptionLicenseType"
    ]
    """<p>The license type for all licenses in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster.</p>"""
    auto_renew: "capo_eks.types.boolean.Boolean"
    """<p>A boolean indicating whether the subscription auto renews at the end of the term.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>The metadata for a subscription to assist with categorization and organization. Each tag consists of a key and an optional value. Subscription tags don't propagate to any other resources associated with the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEksAnywhereSubscriptionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_eks.types.eks_anywhere_subscription_term

    out["term"] = capo_eks.types.eks_anywhere_subscription_term.serialize_json(
        value["term"]
    )
    out["licenseQuantity"] = value.get("license_quantity", 0)
    if "license_type" in value:
        import capo_eks.types.eks_anywhere_subscription_license_type

        out["licenseType"] = (
            capo_eks.types.eks_anywhere_subscription_license_type.serialize_json(
                value["license_type"]
            )
        )
    out["autoRenew"] = value.get("auto_renew", False)
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEksAnywhereSubscriptionRequest:
    out: CreateEksAnywhereSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEksAnywhereSubscriptionRequest.name required")
    if "term" in data:
        import capo_eks.types.eks_anywhere_subscription_term

        out["term"] = capo_eks.types.eks_anywhere_subscription_term.deserialize_json(
            data["term"]
        )
    else:
        raise DeserializationError("CreateEksAnywhereSubscriptionRequest.term required")
    if "licenseQuantity" in data:
        out["license_quantity"] = data["licenseQuantity"]
    else:
        out["license_quantity"] = 0
    if "licenseType" in data:
        import capo_eks.types.eks_anywhere_subscription_license_type

        out["license_type"] = (
            capo_eks.types.eks_anywhere_subscription_license_type.deserialize_json(
                data["licenseType"]
            )
        )
    if "autoRenew" in data:
        out["auto_renew"] = data["autoRenew"]
    else:
        out["auto_renew"] = False
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "tags" in data:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    return out

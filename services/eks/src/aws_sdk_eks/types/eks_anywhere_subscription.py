"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boolean
    import aws_sdk_eks.types.eks_anywhere_subscription_license_type
    import aws_sdk_eks.types.eks_anywhere_subscription_term
    import aws_sdk_eks.types.integer
    import aws_sdk_eks.types.license_list
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list
    import aws_sdk_eks.types.tag_map
    import aws_sdk_eks.types.timestamp


class EksAnywhereSubscription(TypedDict, closed=True):
    id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>UUID identifying a subscription.</p>"""
    arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the subscription.</p>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix timestamp in seconds for when the subscription was created.</p>"""
    effective_date: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix timestamp in seconds for when the subscription is effective.</p>"""
    expiration_date: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix timestamp in seconds for when the subscription will expire or auto renew, depending on the auto renew configuration of the subscription object.</p>"""
    license_quantity: "aws_sdk_eks.types.integer.Integer"
    """<p>The number of licenses included in a subscription. Valid values are between 1 and 100.</p>"""
    license_type: NotRequired[
        "aws_sdk_eks.types.eks_anywhere_subscription_license_type.EksAnywhereSubscriptionLicenseType"
    ]
    """<p>The type of licenses included in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster.</p>"""
    term: NotRequired[
        "aws_sdk_eks.types.eks_anywhere_subscription_term.EksAnywhereSubscriptionTerm"
    ]
    """<p>An EksAnywhereSubscriptionTerm object. </p>"""
    status: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The status of a subscription.</p>"""
    auto_renew: "aws_sdk_eks.types.boolean.Boolean"
    """<p>A boolean indicating whether or not a subscription will auto renew when it expires.</p>"""
    license_arns: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>Amazon Web Services License Manager ARN associated with the subscription.</p>"""
    licenses: NotRequired["aws_sdk_eks.types.license_list.LicenseList"]
    """<p>Includes all of the claims in the license token necessary to validate the license for extended support.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>The metadata for a subscription to assist with categorization and organization. Each tag consists of a key and an optional value. Subscription tags do not propagate to any other resources associated with the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscription) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_eks.types.timestamp

        out["createdAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "effective_date" in value:
        import aws_sdk_eks.types.timestamp

        out["effectiveDate"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["effective_date"]
        )
    if "expiration_date" in value:
        import aws_sdk_eks.types.timestamp

        out["expirationDate"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["expiration_date"]
        )
    out["licenseQuantity"] = value.get("license_quantity", 0)
    if "license_type" in value:
        import aws_sdk_eks.types.eks_anywhere_subscription_license_type

        out["licenseType"] = (
            aws_sdk_eks.types.eks_anywhere_subscription_license_type.serialize_json(
                value["license_type"]
            )
        )
    if "term" in value:
        import aws_sdk_eks.types.eks_anywhere_subscription_term

        out["term"] = aws_sdk_eks.types.eks_anywhere_subscription_term.serialize_json(
            value["term"]
        )
    if "status" in value:
        out["status"] = value["status"]
    out["autoRenew"] = value.get("auto_renew", False)
    if "license_arns" in value:
        import aws_sdk_eks.types.string_list

        out["licenseArns"] = aws_sdk_eks.types.string_list.serialize_json(
            value["license_arns"]
        )
    if "licenses" in value:
        import aws_sdk_eks.types.license_list

        out["licenses"] = aws_sdk_eks.types.license_list.serialize_json(
            value["licenses"]
        )
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EksAnywhereSubscription:
    out: EksAnywhereSubscription = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_eks.types.timestamp

        out["created_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "effectiveDate" in data:
        import aws_sdk_eks.types.timestamp

        out["effective_date"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["effectiveDate"]
        )
    if "expirationDate" in data:
        import aws_sdk_eks.types.timestamp

        out["expiration_date"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["expirationDate"]
        )
    if "licenseQuantity" in data:
        out["license_quantity"] = data["licenseQuantity"]
    else:
        out["license_quantity"] = 0
    if "licenseType" in data:
        import aws_sdk_eks.types.eks_anywhere_subscription_license_type

        out["license_type"] = (
            aws_sdk_eks.types.eks_anywhere_subscription_license_type.deserialize_json(
                data["licenseType"]
            )
        )
    if "term" in data:
        import aws_sdk_eks.types.eks_anywhere_subscription_term

        out["term"] = aws_sdk_eks.types.eks_anywhere_subscription_term.deserialize_json(
            data["term"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "autoRenew" in data:
        out["auto_renew"] = data["autoRenew"]
    else:
        out["auto_renew"] = False
    if "licenseArns" in data:
        import aws_sdk_eks.types.string_list

        out["license_arns"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["licenseArns"]
        )
    if "licenses" in data:
        import aws_sdk_eks.types.license_list

        out["licenses"] = aws_sdk_eks.types.license_list.deserialize_json(
            data["licenses"]
        )
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    return out

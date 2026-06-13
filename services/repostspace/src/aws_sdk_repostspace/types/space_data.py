"""Generated from Smithy shape ``com.amazonaws.repostspace#SpaceData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_repostspace.types.arn
    import aws_sdk_repostspace.types.configuration_status
    import aws_sdk_repostspace.types.content_size
    import aws_sdk_repostspace.types.kms_key
    import aws_sdk_repostspace.types.provisioning_status
    import aws_sdk_repostspace.types.space_description
    import aws_sdk_repostspace.types.space_id
    import aws_sdk_repostspace.types.space_name
    import aws_sdk_repostspace.types.storage_limit
    import aws_sdk_repostspace.types.supported_email_domains_status
    import aws_sdk_repostspace.types.tier_level
    import aws_sdk_repostspace.types.url
    import aws_sdk_repostspace.types.user_count
    import aws_sdk_repostspace.types.vanity_domain_status


class SpaceData(TypedDict):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    arn: "aws_sdk_repostspace.types.arn.Arn"
    """<p>The ARN of the private re:Post.</p>"""
    name: "aws_sdk_repostspace.types.space_name.SpaceName"
    """<p>The name for the private re:Post.</p>"""
    description: NotRequired[
        "aws_sdk_repostspace.types.space_description.SpaceDescription"
    ]
    """<p>The description for the private re:Post. This is used only to help you identify this private re:Post.</p>"""
    status: "aws_sdk_repostspace.types.provisioning_status.ProvisioningStatus"
    """<p>The creation/deletion status of the private re:Post.</p>"""
    configuration_status: (
        "aws_sdk_repostspace.types.configuration_status.ConfigurationStatus"
    )
    """<p>The configuration status of the private re:Post.</p>"""
    vanity_domain_status: (
        "aws_sdk_repostspace.types.vanity_domain_status.VanityDomainStatus"
    )
    """<p>This approval status of the custom subdomain.</p>"""
    vanity_domain: "aws_sdk_repostspace.types.url.Url"
    """<p>This custom subdomain that you use to access your private re:Post. All custom subdomains must be approved by AWS before use.</p>"""
    random_domain: "aws_sdk_repostspace.types.url.Url"
    """<p>The AWS generated subdomain of the private re:Post.</p>"""
    tier: "aws_sdk_repostspace.types.tier_level.TierLevel"
    """<p>The pricing tier of the private re:Post.</p>"""
    storage_limit: "aws_sdk_repostspace.types.storage_limit.StorageLimit"
    """<p>The storage limit of the private re:Post.</p>"""
    create_date_time: "datetime.datetime"
    """<p>The date when the private re:Post was created.</p>"""
    delete_date_time: NotRequired["datetime.datetime"]
    """<p>The date when the private re:Post was deleted.</p>"""
    user_kms_key: NotRequired["aws_sdk_repostspace.types.kms_key.KMSKey"]
    """<p>The custom AWS KMS key ARN that’s used for the AWS KMS encryption.</p>"""
    user_count: NotRequired["aws_sdk_repostspace.types.user_count.UserCount"]
    """<p>The number of onboarded users to the private re:Post.</p>"""
    content_size: NotRequired["aws_sdk_repostspace.types.content_size.ContentSize"]
    """<p>The content size of the private re:Post.</p>"""
    supported_email_domains: NotRequired[
        "aws_sdk_repostspace.types.supported_email_domains_status.SupportedEmailDomainsStatus"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceData) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["status"] = value["status"]
    import aws_sdk_repostspace.types.configuration_status

    out["configurationStatus"] = (
        aws_sdk_repostspace.types.configuration_status.serialize_json(
            value["configuration_status"]
        )
    )
    import aws_sdk_repostspace.types.vanity_domain_status

    out["vanityDomainStatus"] = (
        aws_sdk_repostspace.types.vanity_domain_status.serialize_json(
            value["vanity_domain_status"]
        )
    )
    out["vanityDomain"] = value["vanity_domain"]
    out["randomDomain"] = value["random_domain"]
    import aws_sdk_repostspace.types.tier_level

    out["tier"] = aws_sdk_repostspace.types.tier_level.serialize_json(value["tier"])
    out["storageLimit"] = value["storage_limit"]
    import aws_sdk_repostspace.types._prelude.timestamp

    out["createDateTime"] = aws_sdk_repostspace.types._prelude.timestamp.serialize_json(
        value["create_date_time"]
    )
    if "delete_date_time" in value:
        import aws_sdk_repostspace.types._prelude.timestamp

        out["deleteDateTime"] = (
            aws_sdk_repostspace.types._prelude.timestamp.serialize_json(
                value["delete_date_time"]
            )
        )
    if "user_kms_key" in value:
        out["userKMSKey"] = value["user_kms_key"]
    if "user_count" in value:
        out["userCount"] = value["user_count"]
    if "content_size" in value:
        out["contentSize"] = value["content_size"]
    if "supported_email_domains" in value:
        import aws_sdk_repostspace.types.supported_email_domains_status

        out["supportedEmailDomains"] = (
            aws_sdk_repostspace.types.supported_email_domains_status.serialize_json(
                value["supported_email_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpaceData:
    out: SpaceData = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("SpaceData.space_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SpaceData.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SpaceData.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("SpaceData.status required")
    if "configurationStatus" in data:
        import aws_sdk_repostspace.types.configuration_status

        out["configuration_status"] = (
            aws_sdk_repostspace.types.configuration_status.deserialize_json(
                data["configurationStatus"]
            )
        )
    else:
        raise DeserializationError("SpaceData.configuration_status required")
    if "vanityDomainStatus" in data:
        import aws_sdk_repostspace.types.vanity_domain_status

        out["vanity_domain_status"] = (
            aws_sdk_repostspace.types.vanity_domain_status.deserialize_json(
                data["vanityDomainStatus"]
            )
        )
    else:
        raise DeserializationError("SpaceData.vanity_domain_status required")
    if "vanityDomain" in data:
        out["vanity_domain"] = data["vanityDomain"]
    else:
        raise DeserializationError("SpaceData.vanity_domain required")
    if "randomDomain" in data:
        out["random_domain"] = data["randomDomain"]
    else:
        raise DeserializationError("SpaceData.random_domain required")
    if "tier" in data:
        import aws_sdk_repostspace.types.tier_level

        out["tier"] = aws_sdk_repostspace.types.tier_level.deserialize_json(
            data["tier"]
        )
    else:
        raise DeserializationError("SpaceData.tier required")
    if "storageLimit" in data:
        out["storage_limit"] = data["storageLimit"]
    else:
        raise DeserializationError("SpaceData.storage_limit required")
    if "createDateTime" in data:
        import aws_sdk_repostspace.types._prelude.timestamp

        out["create_date_time"] = (
            aws_sdk_repostspace.types._prelude.timestamp.deserialize_json(
                data["createDateTime"]
            )
        )
    else:
        raise DeserializationError("SpaceData.create_date_time required")
    if "deleteDateTime" in data:
        import aws_sdk_repostspace.types._prelude.timestamp

        out["delete_date_time"] = (
            aws_sdk_repostspace.types._prelude.timestamp.deserialize_json(
                data["deleteDateTime"]
            )
        )
    if "userKMSKey" in data:
        out["user_kms_key"] = data["userKMSKey"]
    if "userCount" in data:
        out["user_count"] = data["userCount"]
    if "contentSize" in data:
        out["content_size"] = data["contentSize"]
    if "supportedEmailDomains" in data:
        import aws_sdk_repostspace.types.supported_email_domains_status

        out["supported_email_domains"] = (
            aws_sdk_repostspace.types.supported_email_domains_status.deserialize_json(
                data["supportedEmailDomains"]
            )
        )
    return out

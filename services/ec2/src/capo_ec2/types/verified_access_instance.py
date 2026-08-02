"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.verified_access_instance_custom_sub_domain
    import capo_ec2.types.verified_access_trust_provider_condensed_list


class VerifiedAccessInstance(TypedDict, closed=True):
    verified_access_instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access instance.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the Amazon Web Services Verified Access instance.</p>"""
    verified_access_trust_providers: NotRequired[
        "capo_ec2.types.verified_access_trust_provider_condensed_list.VerifiedAccessTrustProviderCondensedList"
    ]
    """<p>The IDs of the Amazon Web Services Verified Access trust providers.</p>"""
    creation_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The creation time.</p>"""
    last_updated_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The last updated time.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    fips_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether support for Federal Information Processing Standards (FIPS) is enabled on the instance.</p>"""
    cidr_endpoints_custom_sub_domain: NotRequired[
        "capo_ec2.types.verified_access_instance_custom_sub_domain.VerifiedAccessInstanceCustomSubDomain"
    ]
    """<p>The custom subdomain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "verified_access_trust_providers" in value:
        import capo_ec2.types.verified_access_trust_provider_condensed_list

        capo_ec2.types.verified_access_trust_provider_condensed_list.serialize_ec2_query(
            value["verified_access_trust_providers"],
            pairs,
            f"{key_prefix}VerifiedAccessTrustProviderSet",
        )
    if "creation_time" in value:
        pairs.append((f"{key_prefix}CreationTime", str(value["creation_time"])))
    if "last_updated_time" in value:
        pairs.append((f"{key_prefix}LastUpdatedTime", str(value["last_updated_time"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "fips_enabled" in value:
        pairs.append(
            (f"{key_prefix}FipsEnabled", "true" if value["fips_enabled"] else "false")
        )
    if "cidr_endpoints_custom_sub_domain" in value:
        import capo_ec2.types.verified_access_instance_custom_sub_domain

        capo_ec2.types.verified_access_instance_custom_sub_domain.serialize_ec2_query(
            value["cidr_endpoints_custom_sub_domain"],
            pairs,
            f"{key_prefix}CidrEndpointsCustomSubDomain",
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessInstance:
    out: VerifiedAccessInstance = {}  # type: ignore[typeddict-item]
    child_verified_access_instance_id = el.find("VerifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("VerifiedAccessTrustProviderSet") is not None:
        import capo_ec2.types.verified_access_trust_provider_condensed_list

        out["verified_access_trust_providers"] = (
            capo_ec2.types.verified_access_trust_provider_condensed_list.deserialize_ec2_query(
                el, "VerifiedAccessTrustProviderSet"
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        out["creation_time"] = str(child_creation_time.text or "")
    child_last_updated_time = el.find("LastUpdatedTime")
    if child_last_updated_time is not None:
        out["last_updated_time"] = str(child_last_updated_time.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_fips_enabled = el.find("FipsEnabled")
    if child_fips_enabled is not None:
        out["fips_enabled"] = (child_fips_enabled.text or "").lower() == "true"
    child_cidr_endpoints_custom_sub_domain = el.find("CidrEndpointsCustomSubDomain")
    if child_cidr_endpoints_custom_sub_domain is not None:
        import capo_ec2.types.verified_access_instance_custom_sub_domain

        out["cidr_endpoints_custom_sub_domain"] = (
            capo_ec2.types.verified_access_instance_custom_sub_domain.deserialize_ec2_query(
                child_cidr_endpoints_custom_sub_domain
            )
        )
    return out

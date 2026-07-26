"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionTenant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.customizations
    import capo_cloudfront.types.domain_result_list
    import capo_cloudfront.types.parameters
    import capo_cloudfront.types.string
    import capo_cloudfront.types.tags
    import capo_cloudfront.types.timestamp


class DistributionTenant(TypedDict, closed=True):
    id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the distribution tenant.</p>"""
    distribution_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the multi-tenant distribution.</p>"""
    name: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The name of the distribution tenant.</p>"""
    arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the distribution tenant.</p>"""
    domains: NotRequired["capo_cloudfront.types.domain_result_list.DomainResultList"]
    """<p>The domains associated with the distribution tenant.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]
    customizations: NotRequired["capo_cloudfront.types.customizations.Customizations"]
    """<p>Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.</p>"""
    parameters: NotRequired["capo_cloudfront.types.parameters.Parameters"]
    """<p>A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.</p>"""
    connection_group_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the connection group for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.</p>"""
    created_time: NotRequired["capo_cloudfront.types.timestamp.timestamp"]
    """<p>The date and time when the distribution tenant was created.</p>"""
    last_modified_time: NotRequired["capo_cloudfront.types.timestamp.timestamp"]
    """<p>The date and time when the distribution tenant was updated.</p>"""
    enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant won't serve traffic.</p>"""
    status: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The status of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionTenant, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    if "distribution_id" in value:
        SubElement(el, "DistributionId").text = str(value["distribution_id"])
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "arn" in value:
        SubElement(el, "Arn").text = str(value["arn"])
    if "domains" in value:
        import capo_cloudfront.types.domain_result_list

        capo_cloudfront.types.domain_result_list.serialize_xml(
            value["domains"], el, "Domains"
        )
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")
    if "customizations" in value:
        import capo_cloudfront.types.customizations

        capo_cloudfront.types.customizations.serialize_xml(
            value["customizations"], el, "Customizations"
        )
    if "parameters" in value:
        import capo_cloudfront.types.parameters

        capo_cloudfront.types.parameters.serialize_xml(
            value["parameters"], el, "Parameters"
        )
    if "connection_group_id" in value:
        SubElement(el, "ConnectionGroupId").text = str(value["connection_group_id"])
    if "created_time" in value:
        import capo_cloudfront.types.timestamp

        capo_cloudfront.types.timestamp.serialize_xml(
            value["created_time"], el, "CreatedTime"
        )
    if "last_modified_time" in value:
        import capo_cloudfront.types.timestamp

        capo_cloudfront.types.timestamp.serialize_xml(
            value["last_modified_time"], el, "LastModifiedTime"
        )
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])


def deserialize_xml(el: Element) -> DistributionTenant:
    out: DistributionTenant = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_distribution_id = el.find("DistributionId")
    if child_distribution_id is not None:
        out["distribution_id"] = str(child_distribution_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_domains = el.find("Domains")
    if child_domains is not None:
        import capo_cloudfront.types.domain_result_list

        out["domains"] = capo_cloudfront.types.domain_result_list.deserialize_xml(
            child_domains
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    child_customizations = el.find("Customizations")
    if child_customizations is not None:
        import capo_cloudfront.types.customizations

        out["customizations"] = capo_cloudfront.types.customizations.deserialize_xml(
            child_customizations
        )
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudfront.types.parameters

        out["parameters"] = capo_cloudfront.types.parameters.deserialize_xml(
            child_parameters
        )
    child_connection_group_id = el.find("ConnectionGroupId")
    if child_connection_group_id is not None:
        out["connection_group_id"] = str(child_connection_group_id.text or "")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_cloudfront.types.timestamp

        out["created_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out

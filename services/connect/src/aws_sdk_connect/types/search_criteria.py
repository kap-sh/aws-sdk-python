"""Generated from Smithy shape ``com.amazonaws.connect#SearchCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.active_region_list
    import aws_sdk_connect.types.agent_hierarchy_groups
    import aws_sdk_connect.types.agent_resource_id_list
    import aws_sdk_connect.types.ai_agents_criteria
    import aws_sdk_connect.types.channel_list
    import aws_sdk_connect.types.contact_analysis
    import aws_sdk_connect.types.control_plane_tag_filter
    import aws_sdk_connect.types.initiation_method_list
    import aws_sdk_connect.types.name_criteria
    import aws_sdk_connect.types.queue_id_list
    import aws_sdk_connect.types.search_contacts_additional_time_range
    import aws_sdk_connect.types.searchable_contact_attributes
    import aws_sdk_connect.types.searchable_routing_criteria
    import aws_sdk_connect.types.searchable_segment_attributes


class SearchCriteria(TypedDict):
    name: NotRequired["aws_sdk_connect.types.name_criteria.NameCriteria"]
    """<p>Name of the contact.</p>"""
    agent_ids: NotRequired[
        "aws_sdk_connect.types.agent_resource_id_list.AgentResourceIdList"
    ]
    """<p>The identifiers of agents who handled the contacts.</p>"""
    agent_hierarchy_groups: NotRequired[
        "aws_sdk_connect.types.agent_hierarchy_groups.AgentHierarchyGroups"
    ]
    """<p>The agent hierarchy groups of the agent at the time of handling the contact.</p>"""
    channels: NotRequired["aws_sdk_connect.types.channel_list.ChannelList"]
    """<p>The list of channels associated with contacts.</p>"""
    contact_analysis: NotRequired[
        "aws_sdk_connect.types.contact_analysis.ContactAnalysis"
    ]
    """<p>Search criteria based on analysis outputs from Connect Customer Contact Lens.</p>"""
    initiation_methods: NotRequired[
        "aws_sdk_connect.types.initiation_method_list.InitiationMethodList"
    ]
    """<p>The list of initiation methods associated with contacts.</p>"""
    queue_ids: NotRequired["aws_sdk_connect.types.queue_id_list.QueueIdList"]
    """<p>The list of queue IDs associated with contacts.</p>"""
    routing_criteria: NotRequired[
        "aws_sdk_connect.types.searchable_routing_criteria.SearchableRoutingCriteria"
    ]
    """<p>Routing criteria for the contact.</p>"""
    additional_time_range: NotRequired[
        "aws_sdk_connect.types.search_contacts_additional_time_range.SearchContactsAdditionalTimeRange"
    ]
    """<p>Additional TimeRange used to filter contacts.</p>"""
    searchable_contact_attributes: NotRequired[
        "aws_sdk_connect.types.searchable_contact_attributes.SearchableContactAttributes"
    ]
    r"""<p>The search criteria based on user-defined contact attributes that have been configured for contact search. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/search-custom-attributes.html\">Search by custom contact attributes</a> in the <i>Connect Customer Administrator Guide</i>.</p> <important> <p>To use <code>SearchableContactAttributes</code> in a search request, the <code>GetContactAttributes</code> action is required to perform an API request. For more information, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-actions-as-permissions\">https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-actions-as-permissions</a>Actions defined by Connect Customer.</p> </important>"""
    searchable_segment_attributes: NotRequired[
        "aws_sdk_connect.types.searchable_segment_attributes.SearchableSegmentAttributes"
    ]
    """<p>The search criteria based on searchable segment attributes of a contact.</p>"""
    active_regions: NotRequired[
        "aws_sdk_connect.types.active_region_list.ActiveRegionList"
    ]
    """<p>The list of active regions for contacts in ACGR instances.</p>"""
    contact_tags: NotRequired[
        "aws_sdk_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]
    ai_agents: NotRequired["aws_sdk_connect.types.ai_agents_criteria.AiAgentsCriteria"]
    """<p>AI Agent search criteria definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchCriteria) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_connect.types.name_criteria

        out["Name"] = aws_sdk_connect.types.name_criteria.serialize_json(value["name"])
    if "agent_ids" in value:
        import aws_sdk_connect.types.agent_resource_id_list

        out["AgentIds"] = aws_sdk_connect.types.agent_resource_id_list.serialize_json(
            value["agent_ids"]
        )
    if "agent_hierarchy_groups" in value:
        import aws_sdk_connect.types.agent_hierarchy_groups

        out["AgentHierarchyGroups"] = (
            aws_sdk_connect.types.agent_hierarchy_groups.serialize_json(
                value["agent_hierarchy_groups"]
            )
        )
    if "channels" in value:
        import aws_sdk_connect.types.channel_list

        out["Channels"] = aws_sdk_connect.types.channel_list.serialize_json(
            value["channels"]
        )
    if "contact_analysis" in value:
        import aws_sdk_connect.types.contact_analysis

        out["ContactAnalysis"] = aws_sdk_connect.types.contact_analysis.serialize_json(
            value["contact_analysis"]
        )
    if "initiation_methods" in value:
        import aws_sdk_connect.types.initiation_method_list

        out["InitiationMethods"] = (
            aws_sdk_connect.types.initiation_method_list.serialize_json(
                value["initiation_methods"]
            )
        )
    if "queue_ids" in value:
        import aws_sdk_connect.types.queue_id_list

        out["QueueIds"] = aws_sdk_connect.types.queue_id_list.serialize_json(
            value["queue_ids"]
        )
    if "routing_criteria" in value:
        import aws_sdk_connect.types.searchable_routing_criteria

        out["RoutingCriteria"] = (
            aws_sdk_connect.types.searchable_routing_criteria.serialize_json(
                value["routing_criteria"]
            )
        )
    if "additional_time_range" in value:
        import aws_sdk_connect.types.search_contacts_additional_time_range

        out["AdditionalTimeRange"] = (
            aws_sdk_connect.types.search_contacts_additional_time_range.serialize_json(
                value["additional_time_range"]
            )
        )
    if "searchable_contact_attributes" in value:
        import aws_sdk_connect.types.searchable_contact_attributes

        out["SearchableContactAttributes"] = (
            aws_sdk_connect.types.searchable_contact_attributes.serialize_json(
                value["searchable_contact_attributes"]
            )
        )
    if "searchable_segment_attributes" in value:
        import aws_sdk_connect.types.searchable_segment_attributes

        out["SearchableSegmentAttributes"] = (
            aws_sdk_connect.types.searchable_segment_attributes.serialize_json(
                value["searchable_segment_attributes"]
            )
        )
    if "active_regions" in value:
        import aws_sdk_connect.types.active_region_list

        out["ActiveRegions"] = aws_sdk_connect.types.active_region_list.serialize_json(
            value["active_regions"]
        )
    if "contact_tags" in value:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["ContactTags"] = (
            aws_sdk_connect.types.control_plane_tag_filter.serialize_json(
                value["contact_tags"]
            )
        )
    if "ai_agents" in value:
        import aws_sdk_connect.types.ai_agents_criteria

        out["AiAgents"] = aws_sdk_connect.types.ai_agents_criteria.serialize_json(
            value["ai_agents"]
        )
    return out


def deserialize_json(data: dict) -> SearchCriteria:
    out: SearchCriteria = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_connect.types.name_criteria

        out["name"] = aws_sdk_connect.types.name_criteria.deserialize_json(data["Name"])
    if "AgentIds" in data:
        import aws_sdk_connect.types.agent_resource_id_list

        out["agent_ids"] = (
            aws_sdk_connect.types.agent_resource_id_list.deserialize_json(
                data["AgentIds"]
            )
        )
    if "AgentHierarchyGroups" in data:
        import aws_sdk_connect.types.agent_hierarchy_groups

        out["agent_hierarchy_groups"] = (
            aws_sdk_connect.types.agent_hierarchy_groups.deserialize_json(
                data["AgentHierarchyGroups"]
            )
        )
    if "Channels" in data:
        import aws_sdk_connect.types.channel_list

        out["channels"] = aws_sdk_connect.types.channel_list.deserialize_json(
            data["Channels"]
        )
    if "ContactAnalysis" in data:
        import aws_sdk_connect.types.contact_analysis

        out["contact_analysis"] = (
            aws_sdk_connect.types.contact_analysis.deserialize_json(
                data["ContactAnalysis"]
            )
        )
    if "InitiationMethods" in data:
        import aws_sdk_connect.types.initiation_method_list

        out["initiation_methods"] = (
            aws_sdk_connect.types.initiation_method_list.deserialize_json(
                data["InitiationMethods"]
            )
        )
    if "QueueIds" in data:
        import aws_sdk_connect.types.queue_id_list

        out["queue_ids"] = aws_sdk_connect.types.queue_id_list.deserialize_json(
            data["QueueIds"]
        )
    if "RoutingCriteria" in data:
        import aws_sdk_connect.types.searchable_routing_criteria

        out["routing_criteria"] = (
            aws_sdk_connect.types.searchable_routing_criteria.deserialize_json(
                data["RoutingCriteria"]
            )
        )
    if "AdditionalTimeRange" in data:
        import aws_sdk_connect.types.search_contacts_additional_time_range

        out["additional_time_range"] = (
            aws_sdk_connect.types.search_contacts_additional_time_range.deserialize_json(
                data["AdditionalTimeRange"]
            )
        )
    if "SearchableContactAttributes" in data:
        import aws_sdk_connect.types.searchable_contact_attributes

        out["searchable_contact_attributes"] = (
            aws_sdk_connect.types.searchable_contact_attributes.deserialize_json(
                data["SearchableContactAttributes"]
            )
        )
    if "SearchableSegmentAttributes" in data:
        import aws_sdk_connect.types.searchable_segment_attributes

        out["searchable_segment_attributes"] = (
            aws_sdk_connect.types.searchable_segment_attributes.deserialize_json(
                data["SearchableSegmentAttributes"]
            )
        )
    if "ActiveRegions" in data:
        import aws_sdk_connect.types.active_region_list

        out["active_regions"] = (
            aws_sdk_connect.types.active_region_list.deserialize_json(
                data["ActiveRegions"]
            )
        )
    if "ContactTags" in data:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["contact_tags"] = (
            aws_sdk_connect.types.control_plane_tag_filter.deserialize_json(
                data["ContactTags"]
            )
        )
    if "AiAgents" in data:
        import aws_sdk_connect.types.ai_agents_criteria

        out["ai_agents"] = aws_sdk_connect.types.ai_agents_criteria.deserialize_json(
            data["AiAgents"]
        )
    return out

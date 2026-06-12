"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_get_link_attributes
    import aws_sdk_clouddirectory.types.batch_get_object_attributes
    import aws_sdk_clouddirectory.types.batch_get_object_information
    import aws_sdk_clouddirectory.types.batch_list_attached_indices
    import aws_sdk_clouddirectory.types.batch_list_incoming_typed_links
    import aws_sdk_clouddirectory.types.batch_list_index
    import aws_sdk_clouddirectory.types.batch_list_object_attributes
    import aws_sdk_clouddirectory.types.batch_list_object_children
    import aws_sdk_clouddirectory.types.batch_list_object_parent_paths
    import aws_sdk_clouddirectory.types.batch_list_object_parents
    import aws_sdk_clouddirectory.types.batch_list_object_policies
    import aws_sdk_clouddirectory.types.batch_list_outgoing_typed_links
    import aws_sdk_clouddirectory.types.batch_list_policy_attachments
    import aws_sdk_clouddirectory.types.batch_lookup_policy


class BatchReadOperation(TypedDict):
    list_object_attributes: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_object_attributes.BatchListObjectAttributes"
    ]
    """<p>Lists all attributes that are associated with an object.</p>"""
    list_object_children: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_object_children.BatchListObjectChildren"
    ]
    """<p>Returns a paginated list of child objects that are associated with a given object.</p>"""
    list_attached_indices: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_attached_indices.BatchListAttachedIndices"
    ]
    """<p>Lists indices attached to an object.</p>"""
    list_object_parent_paths: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_object_parent_paths.BatchListObjectParentPaths"
    ]
    """<p>Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html\">Directory Structure</a>.</p>"""
    get_object_information: NotRequired[
        "aws_sdk_clouddirectory.types.batch_get_object_information.BatchGetObjectInformation"
    ]
    """<p>Retrieves metadata about an object.</p>"""
    get_object_attributes: NotRequired[
        "aws_sdk_clouddirectory.types.batch_get_object_attributes.BatchGetObjectAttributes"
    ]
    """<p>Retrieves attributes within a facet that are associated with an object.</p>"""
    list_object_parents: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_object_parents.BatchListObjectParents"
    ]
    """<p>Lists parent objects that are associated with a given object in pagination fashion.</p>"""
    list_object_policies: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_object_policies.BatchListObjectPolicies"
    ]
    """<p>Returns policies attached to an object in pagination fashion.</p>"""
    list_policy_attachments: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_policy_attachments.BatchListPolicyAttachments"
    ]
    """<p>Returns all of the <code>ObjectIdentifiers</code> to which a given policy is attached.</p>"""
    lookup_policy: NotRequired[
        "aws_sdk_clouddirectory.types.batch_lookup_policy.BatchLookupPolicy"
    ]
    """<p>Lists all policies from the root of the <a>Directory</a> to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don't have the policies attached, it returns the <code>ObjectIdentifier</code> for such objects. If policies are present, it returns <code>ObjectIdentifier</code>, <code>policyId</code>, and <code>policyType</code>. Paths that don't lead to the root from the target object are ignored. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies\">Policies</a>.</p>"""
    list_index: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_index.BatchListIndex"
    ]
    """<p>Lists objects attached to the specified index.</p>"""
    list_outgoing_typed_links: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_outgoing_typed_links.BatchListOutgoingTypedLinks"
    ]
    """<p>Returns a paginated list of all the outgoing <a>TypedLinkSpecifier</a> information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>"""
    list_incoming_typed_links: NotRequired[
        "aws_sdk_clouddirectory.types.batch_list_incoming_typed_links.BatchListIncomingTypedLinks"
    ]
    """<p>Returns a paginated list of all the incoming <a>TypedLinkSpecifier</a> information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>"""
    get_link_attributes: NotRequired[
        "aws_sdk_clouddirectory.types.batch_get_link_attributes.BatchGetLinkAttributes"
    ]
    """<p>Retrieves attributes that are associated with a typed link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadOperation) -> dict:
    out: dict = {}
    if "list_object_attributes" in value:
        import aws_sdk_clouddirectory.types.batch_list_object_attributes

        out["ListObjectAttributes"] = (
            aws_sdk_clouddirectory.types.batch_list_object_attributes.serialize_json(
                value["list_object_attributes"]
            )
        )
    if "list_object_children" in value:
        import aws_sdk_clouddirectory.types.batch_list_object_children

        out["ListObjectChildren"] = (
            aws_sdk_clouddirectory.types.batch_list_object_children.serialize_json(
                value["list_object_children"]
            )
        )
    if "list_attached_indices" in value:
        import aws_sdk_clouddirectory.types.batch_list_attached_indices

        out["ListAttachedIndices"] = (
            aws_sdk_clouddirectory.types.batch_list_attached_indices.serialize_json(
                value["list_attached_indices"]
            )
        )
    if "list_object_parent_paths" in value:
        import aws_sdk_clouddirectory.types.batch_list_object_parent_paths

        out["ListObjectParentPaths"] = (
            aws_sdk_clouddirectory.types.batch_list_object_parent_paths.serialize_json(
                value["list_object_parent_paths"]
            )
        )
    if "get_object_information" in value:
        import aws_sdk_clouddirectory.types.batch_get_object_information

        out["GetObjectInformation"] = (
            aws_sdk_clouddirectory.types.batch_get_object_information.serialize_json(
                value["get_object_information"]
            )
        )
    if "get_object_attributes" in value:
        import aws_sdk_clouddirectory.types.batch_get_object_attributes

        out["GetObjectAttributes"] = (
            aws_sdk_clouddirectory.types.batch_get_object_attributes.serialize_json(
                value["get_object_attributes"]
            )
        )
    if "list_object_parents" in value:
        import aws_sdk_clouddirectory.types.batch_list_object_parents

        out["ListObjectParents"] = (
            aws_sdk_clouddirectory.types.batch_list_object_parents.serialize_json(
                value["list_object_parents"]
            )
        )
    if "list_object_policies" in value:
        import aws_sdk_clouddirectory.types.batch_list_object_policies

        out["ListObjectPolicies"] = (
            aws_sdk_clouddirectory.types.batch_list_object_policies.serialize_json(
                value["list_object_policies"]
            )
        )
    if "list_policy_attachments" in value:
        import aws_sdk_clouddirectory.types.batch_list_policy_attachments

        out["ListPolicyAttachments"] = (
            aws_sdk_clouddirectory.types.batch_list_policy_attachments.serialize_json(
                value["list_policy_attachments"]
            )
        )
    if "lookup_policy" in value:
        import aws_sdk_clouddirectory.types.batch_lookup_policy

        out["LookupPolicy"] = (
            aws_sdk_clouddirectory.types.batch_lookup_policy.serialize_json(
                value["lookup_policy"]
            )
        )
    if "list_index" in value:
        import aws_sdk_clouddirectory.types.batch_list_index

        out["ListIndex"] = aws_sdk_clouddirectory.types.batch_list_index.serialize_json(
            value["list_index"]
        )
    if "list_outgoing_typed_links" in value:
        import aws_sdk_clouddirectory.types.batch_list_outgoing_typed_links

        out["ListOutgoingTypedLinks"] = (
            aws_sdk_clouddirectory.types.batch_list_outgoing_typed_links.serialize_json(
                value["list_outgoing_typed_links"]
            )
        )
    if "list_incoming_typed_links" in value:
        import aws_sdk_clouddirectory.types.batch_list_incoming_typed_links

        out["ListIncomingTypedLinks"] = (
            aws_sdk_clouddirectory.types.batch_list_incoming_typed_links.serialize_json(
                value["list_incoming_typed_links"]
            )
        )
    if "get_link_attributes" in value:
        import aws_sdk_clouddirectory.types.batch_get_link_attributes

        out["GetLinkAttributes"] = (
            aws_sdk_clouddirectory.types.batch_get_link_attributes.serialize_json(
                value["get_link_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchReadOperation:
    out: BatchReadOperation = {}  # type: ignore[typeddict-item]
    if "ListObjectAttributes" in data:
        import aws_sdk_clouddirectory.types.batch_list_object_attributes

        out["list_object_attributes"] = (
            aws_sdk_clouddirectory.types.batch_list_object_attributes.deserialize_json(
                data["ListObjectAttributes"]
            )
        )
    if "ListObjectChildren" in data:
        import aws_sdk_clouddirectory.types.batch_list_object_children

        out["list_object_children"] = (
            aws_sdk_clouddirectory.types.batch_list_object_children.deserialize_json(
                data["ListObjectChildren"]
            )
        )
    if "ListAttachedIndices" in data:
        import aws_sdk_clouddirectory.types.batch_list_attached_indices

        out["list_attached_indices"] = (
            aws_sdk_clouddirectory.types.batch_list_attached_indices.deserialize_json(
                data["ListAttachedIndices"]
            )
        )
    if "ListObjectParentPaths" in data:
        import aws_sdk_clouddirectory.types.batch_list_object_parent_paths

        out["list_object_parent_paths"] = (
            aws_sdk_clouddirectory.types.batch_list_object_parent_paths.deserialize_json(
                data["ListObjectParentPaths"]
            )
        )
    if "GetObjectInformation" in data:
        import aws_sdk_clouddirectory.types.batch_get_object_information

        out["get_object_information"] = (
            aws_sdk_clouddirectory.types.batch_get_object_information.deserialize_json(
                data["GetObjectInformation"]
            )
        )
    if "GetObjectAttributes" in data:
        import aws_sdk_clouddirectory.types.batch_get_object_attributes

        out["get_object_attributes"] = (
            aws_sdk_clouddirectory.types.batch_get_object_attributes.deserialize_json(
                data["GetObjectAttributes"]
            )
        )
    if "ListObjectParents" in data:
        import aws_sdk_clouddirectory.types.batch_list_object_parents

        out["list_object_parents"] = (
            aws_sdk_clouddirectory.types.batch_list_object_parents.deserialize_json(
                data["ListObjectParents"]
            )
        )
    if "ListObjectPolicies" in data:
        import aws_sdk_clouddirectory.types.batch_list_object_policies

        out["list_object_policies"] = (
            aws_sdk_clouddirectory.types.batch_list_object_policies.deserialize_json(
                data["ListObjectPolicies"]
            )
        )
    if "ListPolicyAttachments" in data:
        import aws_sdk_clouddirectory.types.batch_list_policy_attachments

        out["list_policy_attachments"] = (
            aws_sdk_clouddirectory.types.batch_list_policy_attachments.deserialize_json(
                data["ListPolicyAttachments"]
            )
        )
    if "LookupPolicy" in data:
        import aws_sdk_clouddirectory.types.batch_lookup_policy

        out["lookup_policy"] = (
            aws_sdk_clouddirectory.types.batch_lookup_policy.deserialize_json(
                data["LookupPolicy"]
            )
        )
    if "ListIndex" in data:
        import aws_sdk_clouddirectory.types.batch_list_index

        out["list_index"] = (
            aws_sdk_clouddirectory.types.batch_list_index.deserialize_json(
                data["ListIndex"]
            )
        )
    if "ListOutgoingTypedLinks" in data:
        import aws_sdk_clouddirectory.types.batch_list_outgoing_typed_links

        out["list_outgoing_typed_links"] = (
            aws_sdk_clouddirectory.types.batch_list_outgoing_typed_links.deserialize_json(
                data["ListOutgoingTypedLinks"]
            )
        )
    if "ListIncomingTypedLinks" in data:
        import aws_sdk_clouddirectory.types.batch_list_incoming_typed_links

        out["list_incoming_typed_links"] = (
            aws_sdk_clouddirectory.types.batch_list_incoming_typed_links.deserialize_json(
                data["ListIncomingTypedLinks"]
            )
        )
    if "GetLinkAttributes" in data:
        import aws_sdk_clouddirectory.types.batch_get_link_attributes

        out["get_link_attributes"] = (
            aws_sdk_clouddirectory.types.batch_get_link_attributes.deserialize_json(
                data["GetLinkAttributes"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_add_facet_to_object
    import aws_sdk_clouddirectory.types.batch_attach_object
    import aws_sdk_clouddirectory.types.batch_attach_policy
    import aws_sdk_clouddirectory.types.batch_attach_to_index
    import aws_sdk_clouddirectory.types.batch_attach_typed_link
    import aws_sdk_clouddirectory.types.batch_create_index
    import aws_sdk_clouddirectory.types.batch_create_object
    import aws_sdk_clouddirectory.types.batch_delete_object
    import aws_sdk_clouddirectory.types.batch_detach_from_index
    import aws_sdk_clouddirectory.types.batch_detach_object
    import aws_sdk_clouddirectory.types.batch_detach_policy
    import aws_sdk_clouddirectory.types.batch_detach_typed_link
    import aws_sdk_clouddirectory.types.batch_remove_facet_from_object
    import aws_sdk_clouddirectory.types.batch_update_link_attributes
    import aws_sdk_clouddirectory.types.batch_update_object_attributes


class BatchWriteOperation(TypedDict, closed=True):
    create_object: NotRequired[
        "aws_sdk_clouddirectory.types.batch_create_object.BatchCreateObject"
    ]
    """<p>Creates an object.</p>"""
    attach_object: NotRequired[
        "aws_sdk_clouddirectory.types.batch_attach_object.BatchAttachObject"
    ]
    """<p>Attaches an object to a <a>Directory</a>.</p>"""
    detach_object: NotRequired[
        "aws_sdk_clouddirectory.types.batch_detach_object.BatchDetachObject"
    ]
    """<p>Detaches an object from a <a>Directory</a>.</p>"""
    update_object_attributes: NotRequired[
        "aws_sdk_clouddirectory.types.batch_update_object_attributes.BatchUpdateObjectAttributes"
    ]
    """<p>Updates a given object's attributes.</p>"""
    delete_object: NotRequired[
        "aws_sdk_clouddirectory.types.batch_delete_object.BatchDeleteObject"
    ]
    """<p>Deletes an object in a <a>Directory</a>.</p>"""
    add_facet_to_object: NotRequired[
        "aws_sdk_clouddirectory.types.batch_add_facet_to_object.BatchAddFacetToObject"
    ]
    """<p>A batch operation that adds a facet to an object.</p>"""
    remove_facet_from_object: NotRequired[
        "aws_sdk_clouddirectory.types.batch_remove_facet_from_object.BatchRemoveFacetFromObject"
    ]
    """<p>A batch operation that removes a facet from an object.</p>"""
    attach_policy: NotRequired[
        "aws_sdk_clouddirectory.types.batch_attach_policy.BatchAttachPolicy"
    ]
    """<p>Attaches a policy object to a regular object. An object can have a limited number of attached policies.</p>"""
    detach_policy: NotRequired[
        "aws_sdk_clouddirectory.types.batch_detach_policy.BatchDetachPolicy"
    ]
    """<p>Detaches a policy from a <a>Directory</a>.</p>"""
    create_index: NotRequired[
        "aws_sdk_clouddirectory.types.batch_create_index.BatchCreateIndex"
    ]
    r"""<p>Creates an index object. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm\">Indexing and search</a> for more information.</p>"""
    attach_to_index: NotRequired[
        "aws_sdk_clouddirectory.types.batch_attach_to_index.BatchAttachToIndex"
    ]
    """<p>Attaches the specified object to the specified index.</p>"""
    detach_from_index: NotRequired[
        "aws_sdk_clouddirectory.types.batch_detach_from_index.BatchDetachFromIndex"
    ]
    """<p>Detaches the specified object from the specified index.</p>"""
    attach_typed_link: NotRequired[
        "aws_sdk_clouddirectory.types.batch_attach_typed_link.BatchAttachTypedLink"
    ]
    r"""<p>Attaches a typed link to a specified source and target object. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>"""
    detach_typed_link: NotRequired[
        "aws_sdk_clouddirectory.types.batch_detach_typed_link.BatchDetachTypedLink"
    ]
    r"""<p>Detaches a typed link from a specified source and target object. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>"""
    update_link_attributes: NotRequired[
        "aws_sdk_clouddirectory.types.batch_update_link_attributes.BatchUpdateLinkAttributes"
    ]
    """<p>Updates a given object's attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteOperation) -> dict:
    out: dict = {}
    if "create_object" in value:
        import aws_sdk_clouddirectory.types.batch_create_object

        out["CreateObject"] = (
            aws_sdk_clouddirectory.types.batch_create_object.serialize_json(
                value["create_object"]
            )
        )
    if "attach_object" in value:
        import aws_sdk_clouddirectory.types.batch_attach_object

        out["AttachObject"] = (
            aws_sdk_clouddirectory.types.batch_attach_object.serialize_json(
                value["attach_object"]
            )
        )
    if "detach_object" in value:
        import aws_sdk_clouddirectory.types.batch_detach_object

        out["DetachObject"] = (
            aws_sdk_clouddirectory.types.batch_detach_object.serialize_json(
                value["detach_object"]
            )
        )
    if "update_object_attributes" in value:
        import aws_sdk_clouddirectory.types.batch_update_object_attributes

        out["UpdateObjectAttributes"] = (
            aws_sdk_clouddirectory.types.batch_update_object_attributes.serialize_json(
                value["update_object_attributes"]
            )
        )
    if "delete_object" in value:
        import aws_sdk_clouddirectory.types.batch_delete_object

        out["DeleteObject"] = (
            aws_sdk_clouddirectory.types.batch_delete_object.serialize_json(
                value["delete_object"]
            )
        )
    if "add_facet_to_object" in value:
        import aws_sdk_clouddirectory.types.batch_add_facet_to_object

        out["AddFacetToObject"] = (
            aws_sdk_clouddirectory.types.batch_add_facet_to_object.serialize_json(
                value["add_facet_to_object"]
            )
        )
    if "remove_facet_from_object" in value:
        import aws_sdk_clouddirectory.types.batch_remove_facet_from_object

        out["RemoveFacetFromObject"] = (
            aws_sdk_clouddirectory.types.batch_remove_facet_from_object.serialize_json(
                value["remove_facet_from_object"]
            )
        )
    if "attach_policy" in value:
        import aws_sdk_clouddirectory.types.batch_attach_policy

        out["AttachPolicy"] = (
            aws_sdk_clouddirectory.types.batch_attach_policy.serialize_json(
                value["attach_policy"]
            )
        )
    if "detach_policy" in value:
        import aws_sdk_clouddirectory.types.batch_detach_policy

        out["DetachPolicy"] = (
            aws_sdk_clouddirectory.types.batch_detach_policy.serialize_json(
                value["detach_policy"]
            )
        )
    if "create_index" in value:
        import aws_sdk_clouddirectory.types.batch_create_index

        out["CreateIndex"] = (
            aws_sdk_clouddirectory.types.batch_create_index.serialize_json(
                value["create_index"]
            )
        )
    if "attach_to_index" in value:
        import aws_sdk_clouddirectory.types.batch_attach_to_index

        out["AttachToIndex"] = (
            aws_sdk_clouddirectory.types.batch_attach_to_index.serialize_json(
                value["attach_to_index"]
            )
        )
    if "detach_from_index" in value:
        import aws_sdk_clouddirectory.types.batch_detach_from_index

        out["DetachFromIndex"] = (
            aws_sdk_clouddirectory.types.batch_detach_from_index.serialize_json(
                value["detach_from_index"]
            )
        )
    if "attach_typed_link" in value:
        import aws_sdk_clouddirectory.types.batch_attach_typed_link

        out["AttachTypedLink"] = (
            aws_sdk_clouddirectory.types.batch_attach_typed_link.serialize_json(
                value["attach_typed_link"]
            )
        )
    if "detach_typed_link" in value:
        import aws_sdk_clouddirectory.types.batch_detach_typed_link

        out["DetachTypedLink"] = (
            aws_sdk_clouddirectory.types.batch_detach_typed_link.serialize_json(
                value["detach_typed_link"]
            )
        )
    if "update_link_attributes" in value:
        import aws_sdk_clouddirectory.types.batch_update_link_attributes

        out["UpdateLinkAttributes"] = (
            aws_sdk_clouddirectory.types.batch_update_link_attributes.serialize_json(
                value["update_link_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchWriteOperation:
    out: BatchWriteOperation = {}  # type: ignore[typeddict-item]
    if "CreateObject" in data:
        import aws_sdk_clouddirectory.types.batch_create_object

        out["create_object"] = (
            aws_sdk_clouddirectory.types.batch_create_object.deserialize_json(
                data["CreateObject"]
            )
        )
    if "AttachObject" in data:
        import aws_sdk_clouddirectory.types.batch_attach_object

        out["attach_object"] = (
            aws_sdk_clouddirectory.types.batch_attach_object.deserialize_json(
                data["AttachObject"]
            )
        )
    if "DetachObject" in data:
        import aws_sdk_clouddirectory.types.batch_detach_object

        out["detach_object"] = (
            aws_sdk_clouddirectory.types.batch_detach_object.deserialize_json(
                data["DetachObject"]
            )
        )
    if "UpdateObjectAttributes" in data:
        import aws_sdk_clouddirectory.types.batch_update_object_attributes

        out["update_object_attributes"] = (
            aws_sdk_clouddirectory.types.batch_update_object_attributes.deserialize_json(
                data["UpdateObjectAttributes"]
            )
        )
    if "DeleteObject" in data:
        import aws_sdk_clouddirectory.types.batch_delete_object

        out["delete_object"] = (
            aws_sdk_clouddirectory.types.batch_delete_object.deserialize_json(
                data["DeleteObject"]
            )
        )
    if "AddFacetToObject" in data:
        import aws_sdk_clouddirectory.types.batch_add_facet_to_object

        out["add_facet_to_object"] = (
            aws_sdk_clouddirectory.types.batch_add_facet_to_object.deserialize_json(
                data["AddFacetToObject"]
            )
        )
    if "RemoveFacetFromObject" in data:
        import aws_sdk_clouddirectory.types.batch_remove_facet_from_object

        out["remove_facet_from_object"] = (
            aws_sdk_clouddirectory.types.batch_remove_facet_from_object.deserialize_json(
                data["RemoveFacetFromObject"]
            )
        )
    if "AttachPolicy" in data:
        import aws_sdk_clouddirectory.types.batch_attach_policy

        out["attach_policy"] = (
            aws_sdk_clouddirectory.types.batch_attach_policy.deserialize_json(
                data["AttachPolicy"]
            )
        )
    if "DetachPolicy" in data:
        import aws_sdk_clouddirectory.types.batch_detach_policy

        out["detach_policy"] = (
            aws_sdk_clouddirectory.types.batch_detach_policy.deserialize_json(
                data["DetachPolicy"]
            )
        )
    if "CreateIndex" in data:
        import aws_sdk_clouddirectory.types.batch_create_index

        out["create_index"] = (
            aws_sdk_clouddirectory.types.batch_create_index.deserialize_json(
                data["CreateIndex"]
            )
        )
    if "AttachToIndex" in data:
        import aws_sdk_clouddirectory.types.batch_attach_to_index

        out["attach_to_index"] = (
            aws_sdk_clouddirectory.types.batch_attach_to_index.deserialize_json(
                data["AttachToIndex"]
            )
        )
    if "DetachFromIndex" in data:
        import aws_sdk_clouddirectory.types.batch_detach_from_index

        out["detach_from_index"] = (
            aws_sdk_clouddirectory.types.batch_detach_from_index.deserialize_json(
                data["DetachFromIndex"]
            )
        )
    if "AttachTypedLink" in data:
        import aws_sdk_clouddirectory.types.batch_attach_typed_link

        out["attach_typed_link"] = (
            aws_sdk_clouddirectory.types.batch_attach_typed_link.deserialize_json(
                data["AttachTypedLink"]
            )
        )
    if "DetachTypedLink" in data:
        import aws_sdk_clouddirectory.types.batch_detach_typed_link

        out["detach_typed_link"] = (
            aws_sdk_clouddirectory.types.batch_detach_typed_link.deserialize_json(
                data["DetachTypedLink"]
            )
        )
    if "UpdateLinkAttributes" in data:
        import aws_sdk_clouddirectory.types.batch_update_link_attributes

        out["update_link_attributes"] = (
            aws_sdk_clouddirectory.types.batch_update_link_attributes.deserialize_json(
                data["UpdateLinkAttributes"]
            )
        )
    return out

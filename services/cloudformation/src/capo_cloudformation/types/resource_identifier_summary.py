"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceIdentifierSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_ids
    import capo_cloudformation.types.resource_identifiers
    import capo_cloudformation.types.resource_type


class ResourceIdentifierSummary(TypedDict, closed=True):
    resource_type: NotRequired["capo_cloudformation.types.resource_type.ResourceType"]
    """<p>The template resource type of the target resources, such as <code>AWS::S3::Bucket</code>.</p>"""
    logical_resource_ids: NotRequired[
        "capo_cloudformation.types.logical_resource_ids.LogicalResourceIds"
    ]
    """<p>The logical IDs of the target resources of the specified <code>ResourceType</code>, as defined in the import template.</p>"""
    resource_identifiers: NotRequired[
        "capo_cloudformation.types.resource_identifiers.ResourceIdentifiers"
    ]
    """<p>The resource properties you can provide during the import to identify your target resources. For example, <code>BucketName</code> is a possible identifier property for <code>AWS::S3::Bucket</code> resources.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceIdentifierSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "logical_resource_ids" in value:
        import capo_cloudformation.types.logical_resource_ids

        capo_cloudformation.types.logical_resource_ids.serialize_query(
            value["logical_resource_ids"], pairs, f"{prefix}.LogicalResourceIds"
        )
    if "resource_identifiers" in value:
        import capo_cloudformation.types.resource_identifiers

        capo_cloudformation.types.resource_identifiers.serialize_query(
            value["resource_identifiers"], pairs, f"{prefix}.ResourceIdentifiers"
        )


def deserialize_query(el: Element) -> ResourceIdentifierSummary:
    out: ResourceIdentifierSummary = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_logical_resource_ids = el.find("LogicalResourceIds")
    if child_logical_resource_ids is not None:
        import capo_cloudformation.types.logical_resource_ids

        out["logical_resource_ids"] = (
            capo_cloudformation.types.logical_resource_ids.deserialize_query(
                child_logical_resource_ids
            )
        )
    child_resource_identifiers = el.find("ResourceIdentifiers")
    if child_resource_identifiers is not None:
        import capo_cloudformation.types.resource_identifiers

        out["resource_identifiers"] = (
            capo_cloudformation.types.resource_identifiers.deserialize_query(
                child_resource_identifiers
            )
        )
    return out

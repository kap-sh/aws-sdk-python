"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.description
    import aws_sdk_cloudformation.types.detection_reason
    import aws_sdk_cloudformation.types.physical_resource_id
    import aws_sdk_cloudformation.types.resource_mapping
    import aws_sdk_cloudformation.types.stack_refactor_action_entity
    import aws_sdk_cloudformation.types.stack_refactor_action_type
    import aws_sdk_cloudformation.types.stack_refactor_detection
    import aws_sdk_cloudformation.types.stack_refactor_resource_identifier
    import aws_sdk_cloudformation.types.stack_refactor_tag_resources
    import aws_sdk_cloudformation.types.stack_refactor_untag_resources


class StackRefactorAction(TypedDict):
    action: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_action_type.StackRefactorActionType"
    ]
    """<p>The action that CloudFormation takes on the stack.</p>"""
    entity: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_action_entity.StackRefactorActionEntity"
    ]
    """<p>The type that will be evaluated in the <code>StackRefactorAction</code>. The following are potential <code>Entity</code> types:</p> <ul> <li> <p> <code>Stack</code> </p> </li> <li> <p> <code>Resource</code> </p> </li> </ul>"""
    physical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The name or unique identifier associated with the physical instance of the resource.</p>"""
    resource_identifier: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_resource_identifier.StackRefactorResourceIdentifier"
    ]
    """<p>A key-value pair that identifies the target resource. The key is an identifier property (for example, <code>BucketName</code> for <code>AWS::S3::Bucket</code> resources) and the value is the actual property value (for example, <code>MyS3Bucket</code>).</p>"""
    description: NotRequired["aws_sdk_cloudformation.types.description.Description"]
    """<p>A description to help you identify the refactor.</p>"""
    detection: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_detection.StackRefactorDetection"
    ]
    """<p>The detection type is one of the following:</p> <ul> <li> <p>Auto: CloudFormation figured out the mapping on its own.</p> </li> <li> <p>Manual: The customer provided the mapping in the <code>ResourceMapping</code> parameter.</p> </li> </ul>"""
    detection_reason: NotRequired[
        "aws_sdk_cloudformation.types.detection_reason.DetectionReason"
    ]
    """<p>The description of the detection type.</p>"""
    tag_resources: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_tag_resources.StackRefactorTagResources"
    ]
    """<p>Assigns one or more tags to specified resources.</p>"""
    untag_resources: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_untag_resources.StackRefactorUntagResources"
    ]
    """<p>Removes one or more tags to specified resources.</p>"""
    resource_mapping: NotRequired[
        "aws_sdk_cloudformation.types.resource_mapping.ResourceMapping"
    ]
    """<p>The mapping for the stack resource <code>Source</code> and stack resource <code>Destination</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackRefactorAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "action" in value:
        import aws_sdk_cloudformation.types.stack_refactor_action_type

        aws_sdk_cloudformation.types.stack_refactor_action_type.serialize_query(
            value["action"], pairs, f"{prefix}.Action"
        )
    if "entity" in value:
        import aws_sdk_cloudformation.types.stack_refactor_action_entity

        aws_sdk_cloudformation.types.stack_refactor_action_entity.serialize_query(
            value["entity"], pairs, f"{prefix}.Entity"
        )
    if "physical_resource_id" in value:
        pairs.append(
            (f"{prefix}.PhysicalResourceId", str(value["physical_resource_id"]))
        )
    if "resource_identifier" in value:
        pairs.append(
            (f"{prefix}.ResourceIdentifier", str(value["resource_identifier"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "detection" in value:
        import aws_sdk_cloudformation.types.stack_refactor_detection

        aws_sdk_cloudformation.types.stack_refactor_detection.serialize_query(
            value["detection"], pairs, f"{prefix}.Detection"
        )
    if "detection_reason" in value:
        pairs.append((f"{prefix}.DetectionReason", str(value["detection_reason"])))
    if "tag_resources" in value:
        import aws_sdk_cloudformation.types.stack_refactor_tag_resources

        aws_sdk_cloudformation.types.stack_refactor_tag_resources.serialize_query(
            value["tag_resources"], pairs, f"{prefix}.TagResources"
        )
    if "untag_resources" in value:
        import aws_sdk_cloudformation.types.stack_refactor_untag_resources

        aws_sdk_cloudformation.types.stack_refactor_untag_resources.serialize_query(
            value["untag_resources"], pairs, f"{prefix}.UntagResources"
        )
    if "resource_mapping" in value:
        import aws_sdk_cloudformation.types.resource_mapping

        aws_sdk_cloudformation.types.resource_mapping.serialize_query(
            value["resource_mapping"], pairs, f"{prefix}.ResourceMapping"
        )


def deserialize_query(el: Element) -> StackRefactorAction:
    out: StackRefactorAction = {}  # type: ignore[typeddict-item]
    child_action = el.find("Action")
    if child_action is not None:
        import aws_sdk_cloudformation.types.stack_refactor_action_type

        out["action"] = (
            aws_sdk_cloudformation.types.stack_refactor_action_type.deserialize_query(
                child_action
            )
        )
    child_entity = el.find("Entity")
    if child_entity is not None:
        import aws_sdk_cloudformation.types.stack_refactor_action_entity

        out["entity"] = (
            aws_sdk_cloudformation.types.stack_refactor_action_entity.deserialize_query(
                child_entity
            )
        )
    child_physical_resource_id = el.find("PhysicalResourceId")
    if child_physical_resource_id is not None:
        out["physical_resource_id"] = str(child_physical_resource_id.text or "")
    child_resource_identifier = el.find("ResourceIdentifier")
    if child_resource_identifier is not None:
        out["resource_identifier"] = str(child_resource_identifier.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_detection = el.find("Detection")
    if child_detection is not None:
        import aws_sdk_cloudformation.types.stack_refactor_detection

        out["detection"] = (
            aws_sdk_cloudformation.types.stack_refactor_detection.deserialize_query(
                child_detection
            )
        )
    child_detection_reason = el.find("DetectionReason")
    if child_detection_reason is not None:
        out["detection_reason"] = str(child_detection_reason.text or "")
    child_tag_resources = el.find("TagResources")
    if child_tag_resources is not None:
        import aws_sdk_cloudformation.types.stack_refactor_tag_resources

        out["tag_resources"] = (
            aws_sdk_cloudformation.types.stack_refactor_tag_resources.deserialize_query(
                child_tag_resources
            )
        )
    child_untag_resources = el.find("UntagResources")
    if child_untag_resources is not None:
        import aws_sdk_cloudformation.types.stack_refactor_untag_resources

        out["untag_resources"] = (
            aws_sdk_cloudformation.types.stack_refactor_untag_resources.deserialize_query(
                child_untag_resources
            )
        )
    child_resource_mapping = el.find("ResourceMapping")
    if child_resource_mapping is not None:
        import aws_sdk_cloudformation.types.resource_mapping

        out["resource_mapping"] = (
            aws_sdk_cloudformation.types.resource_mapping.deserialize_query(
                child_resource_mapping
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_set_id
    import capo_cloudformation.types.change_set_name
    import capo_cloudformation.types.change_set_status
    import capo_cloudformation.types.change_set_status_reason
    import capo_cloudformation.types.creation_time
    import capo_cloudformation.types.description
    import capo_cloudformation.types.execution_status
    import capo_cloudformation.types.import_existing_resources
    import capo_cloudformation.types.include_nested_stacks
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_name


class ChangeSetSummary(TypedDict, closed=True):
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>The ID of the stack with which the change set is associated.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name of the stack with which the change set is associated.</p>"""
    change_set_id: NotRequired["capo_cloudformation.types.change_set_id.ChangeSetId"]
    """<p>The ID of the change set.</p>"""
    change_set_name: NotRequired[
        "capo_cloudformation.types.change_set_name.ChangeSetName"
    ]
    """<p>The name of the change set.</p>"""
    execution_status: NotRequired[
        "capo_cloudformation.types.execution_status.ExecutionStatus"
    ]
    """<p>If the change set execution status is <code>AVAILABLE</code>, you can execute the change set. If you can't execute the change set, the status indicates why. For example, a change set might be in an <code>UNAVAILABLE</code> state because CloudFormation is still creating it or in an <code>OBSOLETE</code> state because the stack was already updated.</p>"""
    status: NotRequired["capo_cloudformation.types.change_set_status.ChangeSetStatus"]
    """<p>The state of the change set, such as <code>CREATE_PENDING</code>, <code>CREATE_COMPLETE</code>, or <code>FAILED</code>.</p>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.change_set_status_reason.ChangeSetStatusReason"
    ]
    """<p>A description of the change set's status. For example, if your change set is in the <code>FAILED</code> state, CloudFormation shows the error message.</p>"""
    creation_time: NotRequired["capo_cloudformation.types.creation_time.CreationTime"]
    """<p>The start time when the change set was created, in UTC.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>Descriptive information about the change set.</p>"""
    include_nested_stacks: NotRequired[
        "capo_cloudformation.types.include_nested_stacks.IncludeNestedStacks"
    ]
    """<p>Specifies the current setting of <code>IncludeNestedStacks</code> for the change set.</p>"""
    parent_change_set_id: NotRequired[
        "capo_cloudformation.types.change_set_id.ChangeSetId"
    ]
    """<p>The parent change set ID.</p>"""
    root_change_set_id: NotRequired[
        "capo_cloudformation.types.change_set_id.ChangeSetId"
    ]
    """<p>The root change set ID.</p>"""
    import_existing_resources: NotRequired[
        "capo_cloudformation.types.import_existing_resources.ImportExistingResources"
    ]
    """<p>Indicates if the change set imports resources that already exist.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_id" in value:
        pairs.append((f"{prefix}.StackId", str(value["stack_id"])))
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "change_set_id" in value:
        pairs.append((f"{prefix}.ChangeSetId", str(value["change_set_id"])))
    if "change_set_name" in value:
        pairs.append((f"{prefix}.ChangeSetName", str(value["change_set_name"])))
    if "execution_status" in value:
        import capo_cloudformation.types.execution_status

        capo_cloudformation.types.execution_status.serialize_query(
            value["execution_status"], pairs, f"{prefix}.ExecutionStatus"
        )
    if "status" in value:
        import capo_cloudformation.types.change_set_status

        capo_cloudformation.types.change_set_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_reason" in value:
        pairs.append((f"{prefix}.StatusReason", str(value["status_reason"])))
    if "creation_time" in value:
        import capo_cloudformation.types.creation_time

        capo_cloudformation.types.creation_time.serialize_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "include_nested_stacks" in value:
        pairs.append(
            (
                f"{prefix}.IncludeNestedStacks",
                "true" if value["include_nested_stacks"] else "false",
            )
        )
    if "parent_change_set_id" in value:
        pairs.append(
            (f"{prefix}.ParentChangeSetId", str(value["parent_change_set_id"]))
        )
    if "root_change_set_id" in value:
        pairs.append((f"{prefix}.RootChangeSetId", str(value["root_change_set_id"])))
    if "import_existing_resources" in value:
        pairs.append(
            (
                f"{prefix}.ImportExistingResources",
                "true" if value["import_existing_resources"] else "false",
            )
        )


def deserialize_query(el: Element) -> ChangeSetSummary:
    out: ChangeSetSummary = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_change_set_id = el.find("ChangeSetId")
    if child_change_set_id is not None:
        out["change_set_id"] = str(child_change_set_id.text or "")
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_execution_status = el.find("ExecutionStatus")
    if child_execution_status is not None:
        import capo_cloudformation.types.execution_status

        out["execution_status"] = (
            capo_cloudformation.types.execution_status.deserialize_query(
                child_execution_status
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.change_set_status

        out["status"] = capo_cloudformation.types.change_set_status.deserialize_query(
            child_status
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_cloudformation.types.creation_time

        out["creation_time"] = (
            capo_cloudformation.types.creation_time.deserialize_query(
                child_creation_time
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_include_nested_stacks = el.find("IncludeNestedStacks")
    if child_include_nested_stacks is not None:
        out["include_nested_stacks"] = (
            child_include_nested_stacks.text or ""
        ).lower() == "true"
    child_parent_change_set_id = el.find("ParentChangeSetId")
    if child_parent_change_set_id is not None:
        out["parent_change_set_id"] = str(child_parent_change_set_id.text or "")
    child_root_change_set_id = el.find("RootChangeSetId")
    if child_root_change_set_id is not None:
        out["root_change_set_id"] = str(child_root_change_set_id.text or "")
    child_import_existing_resources = el.find("ImportExistingResources")
    if child_import_existing_resources is not None:
        out["import_existing_resources"] = (
            child_import_existing_resources.text or ""
        ).lower() == "true"
    return out

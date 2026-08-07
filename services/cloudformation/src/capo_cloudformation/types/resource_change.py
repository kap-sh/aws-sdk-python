"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.after_context
    import capo_cloudformation.types.before_context
    import capo_cloudformation.types.change_action
    import capo_cloudformation.types.change_set_id
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.module_info
    import capo_cloudformation.types.physical_resource_id
    import capo_cloudformation.types.policy_action
    import capo_cloudformation.types.previous_deployment_context
    import capo_cloudformation.types.replacement
    import capo_cloudformation.types.resource_change_details
    import capo_cloudformation.types.resource_drift_ignored_attributes
    import capo_cloudformation.types.resource_type
    import capo_cloudformation.types.scope
    import capo_cloudformation.types.stack_resource_drift_status


class ResourceChange(TypedDict, closed=True):
    policy_action: NotRequired["capo_cloudformation.types.policy_action.PolicyAction"]
    """<p>The action that will be taken on the physical resource when the change set is executed.</p> <ul> <li> <p> <code>Delete</code> The resource will be deleted.</p> </li> <li> <p> <code>Retain</code> The resource will be retained.</p> </li> <li> <p> <code>Snapshot</code> The resource will have a snapshot taken.</p> </li> <li> <p> <code>ReplaceAndDelete</code> The resource will be replaced and then deleted.</p> </li> <li> <p> <code>ReplaceAndRetain</code> The resource will be replaced and then retained.</p> </li> <li> <p> <code>ReplaceAndSnapshot</code> The resource will be replaced and then have a snapshot taken.</p> </li> </ul>"""
    action: NotRequired["capo_cloudformation.types.change_action.ChangeAction"]
    """<p>The action that CloudFormation takes on the resource, such as <code>Add</code> (adds a new resource), <code>Modify</code> (changes a resource), <code>Remove</code> (deletes a resource), <code>Import</code> (imports a resource), <code>Dynamic</code> (exact action for the resource can't be determined), or <code>SyncWithActual</code> (resource will not be changed, only CloudFormation metadata will change).</p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The resource's logical ID, which is defined in the stack's template.</p>"""
    physical_resource_id: NotRequired[
        "capo_cloudformation.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The resource's physical ID (resource name). Resources that you are adding don't have physical IDs because they haven't been created.</p>"""
    resource_type: NotRequired["capo_cloudformation.types.resource_type.ResourceType"]
    """<p>The type of CloudFormation resource, such as <code>AWS::S3::Bucket</code>.</p>"""
    replacement: NotRequired["capo_cloudformation.types.replacement.Replacement"]
    """<p>For the <code>Modify</code> action, indicates whether CloudFormation will replace the resource by creating a new one and deleting the old one. This value depends on the value of the <code>RequiresRecreation</code> property in the <code>ResourceTargetDefinition</code> structure. For example, if the <code>RequiresRecreation</code> field is <code>Always</code> and the <code>Evaluation</code> field is <code>Static</code>, <code>Replacement</code> is <code>True</code>. If the <code>RequiresRecreation</code> field is <code>Always</code> and the <code>Evaluation</code> field is <code>Dynamic</code>, <code>Replacement</code> is <code>Conditional</code>.</p> <p>If you have multiple changes with different <code>RequiresRecreation</code> values, the <code>Replacement</code> value depends on the change with the most impact. A <code>RequiresRecreation</code> value of <code>Always</code> has the most impact, followed by <code>Conditional</code>, and then <code>Never</code>.</p>"""
    scope: NotRequired["capo_cloudformation.types.scope.Scope"]
    """<p>For the <code>Modify</code> action, indicates which resource attribute is triggering this update, such as a change in the resource attribute's <code>Metadata</code>, <code>Properties</code>, or <code>Tags</code>.</p>"""
    resource_drift_status: NotRequired[
        "capo_cloudformation.types.stack_resource_drift_status.StackResourceDriftStatus"
    ]
    """<p>The drift status of the resource. Valid values:</p> <ul> <li> <p> <code>IN_SYNC</code> – The resource matches its template definition.</p> </li> <li> <p> <code>MODIFIED</code> – Resource properties were modified outside CloudFormation.</p> </li> <li> <p> <code>DELETED</code> – The resource was deleted outside CloudFormation.</p> </li> <li> <p> <code>NOT_CHECKED</code> – CloudFormation doesn’t currently return this value.</p> </li> <li> <p> <code>UNKNOWN</code> – Drift status could not be determined.</p> </li> <li> <p> <code>UNSUPPORTED</code> – Resource type does not support actual state comparison.</p> </li> </ul> <p>Only present for drift-aware change sets.</p>"""
    resource_drift_ignored_attributes: NotRequired[
        "capo_cloudformation.types.resource_drift_ignored_attributes.ResourceDriftIgnoredAttributes"
    ]
    """<p>List of resource attributes for which drift was ignored.</p>"""
    details: NotRequired[
        "capo_cloudformation.types.resource_change_details.ResourceChangeDetails"
    ]
    """<p>For the <code>Modify</code> action, a list of <code>ResourceChangeDetail</code> structures that describes the changes that CloudFormation will make to the resource.</p>"""
    change_set_id: NotRequired["capo_cloudformation.types.change_set_id.ChangeSetId"]
    """<p>The change set ID of the nested change set.</p>"""
    module_info: NotRequired["capo_cloudformation.types.module_info.ModuleInfo"]
    """<p>Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.</p>"""
    before_context: NotRequired[
        "capo_cloudformation.types.before_context.BeforeContext"
    ]
    """<p>An encoded JSON string that contains the context of the resource before the change is executed.</p>"""
    after_context: NotRequired["capo_cloudformation.types.after_context.AfterContext"]
    """<p>An encoded JSON string that contains the context of the resource after the change is executed.</p>"""
    previous_deployment_context: NotRequired[
        "capo_cloudformation.types.previous_deployment_context.PreviousDeploymentContext"
    ]
    """<p>Information about the resource's state from the previous CloudFormation deployment.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceChange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_action" in value:
        import capo_cloudformation.types.policy_action

        capo_cloudformation.types.policy_action.serialize_query(
            value["policy_action"], pairs, f"{key_prefix}PolicyAction"
        )
    if "action" in value:
        import capo_cloudformation.types.change_action

        capo_cloudformation.types.change_action.serialize_query(
            value["action"], pairs, f"{key_prefix}Action"
        )
    if "logical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}LogicalResourceId", str(value["logical_resource_id"]))
        )
    if "physical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}PhysicalResourceId", str(value["physical_resource_id"]))
        )
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "replacement" in value:
        import capo_cloudformation.types.replacement

        capo_cloudformation.types.replacement.serialize_query(
            value["replacement"], pairs, f"{key_prefix}Replacement"
        )
    if "scope" in value:
        import capo_cloudformation.types.scope

        capo_cloudformation.types.scope.serialize_query(
            value["scope"], pairs, f"{key_prefix}Scope"
        )
    if "resource_drift_status" in value:
        import capo_cloudformation.types.stack_resource_drift_status

        capo_cloudformation.types.stack_resource_drift_status.serialize_query(
            value["resource_drift_status"], pairs, f"{key_prefix}ResourceDriftStatus"
        )
    if "resource_drift_ignored_attributes" in value:
        import capo_cloudformation.types.resource_drift_ignored_attributes

        capo_cloudformation.types.resource_drift_ignored_attributes.serialize_query(
            value["resource_drift_ignored_attributes"],
            pairs,
            f"{key_prefix}ResourceDriftIgnoredAttributes",
        )
    if "details" in value:
        import capo_cloudformation.types.resource_change_details

        capo_cloudformation.types.resource_change_details.serialize_query(
            value["details"], pairs, f"{key_prefix}Details"
        )
    if "change_set_id" in value:
        pairs.append((f"{key_prefix}ChangeSetId", str(value["change_set_id"])))
    if "module_info" in value:
        import capo_cloudformation.types.module_info

        capo_cloudformation.types.module_info.serialize_query(
            value["module_info"], pairs, f"{key_prefix}ModuleInfo"
        )
    if "before_context" in value:
        pairs.append((f"{key_prefix}BeforeContext", str(value["before_context"])))
    if "after_context" in value:
        pairs.append((f"{key_prefix}AfterContext", str(value["after_context"])))
    if "previous_deployment_context" in value:
        pairs.append(
            (
                f"{key_prefix}PreviousDeploymentContext",
                str(value["previous_deployment_context"]),
            )
        )


def deserialize_query(el: Element) -> ResourceChange:
    out: ResourceChange = {}  # type: ignore[typeddict-item]
    child_policy_action = el.find("PolicyAction")
    if child_policy_action is not None:
        import capo_cloudformation.types.policy_action

        out["policy_action"] = (
            capo_cloudformation.types.policy_action.deserialize_query(
                child_policy_action
            )
        )
    child_action = el.find("Action")
    if child_action is not None:
        import capo_cloudformation.types.change_action

        out["action"] = capo_cloudformation.types.change_action.deserialize_query(
            child_action
        )
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_physical_resource_id = el.find("PhysicalResourceId")
    if child_physical_resource_id is not None:
        out["physical_resource_id"] = str(child_physical_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_replacement = el.find("Replacement")
    if child_replacement is not None:
        import capo_cloudformation.types.replacement

        out["replacement"] = capo_cloudformation.types.replacement.deserialize_query(
            child_replacement
        )
    child_scope = el.find("Scope")
    if child_scope is not None:
        import capo_cloudformation.types.scope

        out["scope"] = capo_cloudformation.types.scope.deserialize_query(child_scope)
    child_resource_drift_status = el.find("ResourceDriftStatus")
    if child_resource_drift_status is not None:
        import capo_cloudformation.types.stack_resource_drift_status

        out["resource_drift_status"] = (
            capo_cloudformation.types.stack_resource_drift_status.deserialize_query(
                child_resource_drift_status
            )
        )
    child_resource_drift_ignored_attributes = el.find("ResourceDriftIgnoredAttributes")
    if child_resource_drift_ignored_attributes is not None:
        import capo_cloudformation.types.resource_drift_ignored_attributes

        out["resource_drift_ignored_attributes"] = (
            capo_cloudformation.types.resource_drift_ignored_attributes.deserialize_query(
                child_resource_drift_ignored_attributes
            )
        )
    child_details = el.find("Details")
    if child_details is not None:
        import capo_cloudformation.types.resource_change_details

        out["details"] = (
            capo_cloudformation.types.resource_change_details.deserialize_query(
                child_details
            )
        )
    child_change_set_id = el.find("ChangeSetId")
    if child_change_set_id is not None:
        out["change_set_id"] = str(child_change_set_id.text or "")
    child_module_info = el.find("ModuleInfo")
    if child_module_info is not None:
        import capo_cloudformation.types.module_info

        out["module_info"] = capo_cloudformation.types.module_info.deserialize_query(
            child_module_info
        )
    child_before_context = el.find("BeforeContext")
    if child_before_context is not None:
        out["before_context"] = str(child_before_context.text or "")
    child_after_context = el.find("AfterContext")
    if child_after_context is not None:
        out["after_context"] = str(child_after_context.text or "")
    child_previous_deployment_context = el.find("PreviousDeploymentContext")
    if child_previous_deployment_context is not None:
        out["previous_deployment_context"] = str(
            child_previous_deployment_context.text or ""
        )
    return out

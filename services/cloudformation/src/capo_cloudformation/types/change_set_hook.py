"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetHook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_set_hook_target_details
    import capo_cloudformation.types.hook_failure_mode
    import capo_cloudformation.types.hook_invocation_point
    import capo_cloudformation.types.hook_type_configuration_version_id
    import capo_cloudformation.types.hook_type_name
    import capo_cloudformation.types.hook_type_version_id


class ChangeSetHook(TypedDict, closed=True):
    invocation_point: NotRequired[
        "capo_cloudformation.types.hook_invocation_point.HookInvocationPoint"
    ]
    """<p>The specific point in the provisioning process where the Hook is invoked.</p>"""
    failure_mode: NotRequired[
        "capo_cloudformation.types.hook_failure_mode.HookFailureMode"
    ]
    """<p>Specify the Hook failure mode for non-compliant resources in the followings ways.</p> <ul> <li> <p> <code>FAIL</code> Stops provisioning resources.</p> </li> <li> <p> <code>WARN</code> Allows provisioning to continue with a warning message.</p> </li> </ul>"""
    type_name: NotRequired["capo_cloudformation.types.hook_type_name.HookTypeName"]
    """<p>The unique name for your Hook. Specifies a three-part namespace for your Hook, with a recommended pattern of <code>Organization::Service::Hook</code>.</p> <note> <p>The following organization namespaces are reserved and can't be used in your Hook type names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>ASK</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>"""
    type_version_id: NotRequired[
        "capo_cloudformation.types.hook_type_version_id.HookTypeVersionId"
    ]
    """<p>The version ID of the type specified.</p>"""
    type_configuration_version_id: NotRequired[
        "capo_cloudformation.types.hook_type_configuration_version_id.HookTypeConfigurationVersionId"
    ]
    """<p>The version ID of the type configuration.</p>"""
    target_details: NotRequired[
        "capo_cloudformation.types.change_set_hook_target_details.ChangeSetHookTargetDetails"
    ]
    """<p>Specifies details about the target that the Hook will run against.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetHook, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "invocation_point" in value:
        import capo_cloudformation.types.hook_invocation_point

        capo_cloudformation.types.hook_invocation_point.serialize_query(
            value["invocation_point"], pairs, f"{key_prefix}InvocationPoint"
        )
    if "failure_mode" in value:
        import capo_cloudformation.types.hook_failure_mode

        capo_cloudformation.types.hook_failure_mode.serialize_query(
            value["failure_mode"], pairs, f"{key_prefix}FailureMode"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "type_version_id" in value:
        pairs.append((f"{key_prefix}TypeVersionId", str(value["type_version_id"])))
    if "type_configuration_version_id" in value:
        pairs.append(
            (
                f"{key_prefix}TypeConfigurationVersionId",
                str(value["type_configuration_version_id"]),
            )
        )
    if "target_details" in value:
        import capo_cloudformation.types.change_set_hook_target_details

        capo_cloudformation.types.change_set_hook_target_details.serialize_query(
            value["target_details"], pairs, f"{key_prefix}TargetDetails"
        )


def deserialize_query(el: Element) -> ChangeSetHook:
    out: ChangeSetHook = {}  # type: ignore[typeddict-item]
    child_invocation_point = el.find("InvocationPoint")
    if child_invocation_point is not None:
        import capo_cloudformation.types.hook_invocation_point

        out["invocation_point"] = (
            capo_cloudformation.types.hook_invocation_point.deserialize_query(
                child_invocation_point
            )
        )
    child_failure_mode = el.find("FailureMode")
    if child_failure_mode is not None:
        import capo_cloudformation.types.hook_failure_mode

        out["failure_mode"] = (
            capo_cloudformation.types.hook_failure_mode.deserialize_query(
                child_failure_mode
            )
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_type_version_id = el.find("TypeVersionId")
    if child_type_version_id is not None:
        out["type_version_id"] = str(child_type_version_id.text or "")
    child_type_configuration_version_id = el.find("TypeConfigurationVersionId")
    if child_type_configuration_version_id is not None:
        out["type_configuration_version_id"] = str(
            child_type_configuration_version_id.text or ""
        )
    child_target_details = el.find("TargetDetails")
    if child_target_details is not None:
        import capo_cloudformation.types.change_set_hook_target_details

        out["target_details"] = (
            capo_cloudformation.types.change_set_hook_target_details.deserialize_query(
                child_target_details
            )
        )
    return out

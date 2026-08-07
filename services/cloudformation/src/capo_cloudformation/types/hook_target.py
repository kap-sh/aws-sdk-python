"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.hook_target_action
    import capo_cloudformation.types.hook_target_id
    import capo_cloudformation.types.hook_target_type
    import capo_cloudformation.types.hook_target_type_name


class HookTarget(TypedDict, closed=True):
    target_type: NotRequired[
        "capo_cloudformation.types.hook_target_type.HookTargetType"
    ]
    """<p>The target type.</p>"""
    target_type_name: NotRequired[
        "capo_cloudformation.types.hook_target_type_name.HookTargetTypeName"
    ]
    """<p>The target name, for example, <code>AWS::S3::Bucket</code>.</p>"""
    target_id: NotRequired["capo_cloudformation.types.hook_target_id.HookTargetId"]
    """<p>The unique identifier of the Hook invocation target.</p>"""
    action: NotRequired["capo_cloudformation.types.hook_target_action.HookTargetAction"]
    """<p>The action that invoked the Hook.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HookTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_type" in value:
        import capo_cloudformation.types.hook_target_type

        capo_cloudformation.types.hook_target_type.serialize_query(
            value["target_type"], pairs, f"{key_prefix}TargetType"
        )
    if "target_type_name" in value:
        pairs.append((f"{key_prefix}TargetTypeName", str(value["target_type_name"])))
    if "target_id" in value:
        pairs.append((f"{key_prefix}TargetId", str(value["target_id"])))
    if "action" in value:
        import capo_cloudformation.types.hook_target_action

        capo_cloudformation.types.hook_target_action.serialize_query(
            value["action"], pairs, f"{key_prefix}Action"
        )


def deserialize_query(el: Element) -> HookTarget:
    out: HookTarget = {}  # type: ignore[typeddict-item]
    child_target_type = el.find("TargetType")
    if child_target_type is not None:
        import capo_cloudformation.types.hook_target_type

        out["target_type"] = (
            capo_cloudformation.types.hook_target_type.deserialize_query(
                child_target_type
            )
        )
    child_target_type_name = el.find("TargetTypeName")
    if child_target_type_name is not None:
        out["target_type_name"] = str(child_target_type_name.text or "")
    child_target_id = el.find("TargetId")
    if child_target_id is not None:
        out["target_id"] = str(child_target_id.text or "")
    child_action = el.find("Action")
    if child_action is not None:
        import capo_cloudformation.types.hook_target_action

        out["action"] = capo_cloudformation.types.hook_target_action.deserialize_query(
            child_action
        )
    return out

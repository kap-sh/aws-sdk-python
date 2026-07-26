"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplyEnvironmentManagedActionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.action_type
    import capo_elastic_beanstalk.types.string


class ApplyEnvironmentManagedActionResult(TypedDict, closed=True):
    action_id: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The action ID of the managed action.</p>"""
    action_description: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>A description of the managed action.</p>"""
    action_type: NotRequired["capo_elastic_beanstalk.types.action_type.ActionType"]
    """<p>The type of managed action.</p>"""
    status: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The status of the managed action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplyEnvironmentManagedActionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "action_id" in value:
        pairs.append((f"{prefix}.ActionId", str(value["action_id"])))
    if "action_description" in value:
        pairs.append((f"{prefix}.ActionDescription", str(value["action_description"])))
    if "action_type" in value:
        import capo_elastic_beanstalk.types.action_type

        capo_elastic_beanstalk.types.action_type.serialize_query(
            value["action_type"], pairs, f"{prefix}.ActionType"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> ApplyEnvironmentManagedActionResult:
    out: ApplyEnvironmentManagedActionResult = {}  # type: ignore[typeddict-item]
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    child_action_description = el.find("ActionDescription")
    if child_action_description is not None:
        out["action_description"] = str(child_action_description.text or "")
    child_action_type = el.find("ActionType")
    if child_action_type is not None:
        import capo_elastic_beanstalk.types.action_type

        out["action_type"] = capo_elastic_beanstalk.types.action_type.deserialize_query(
            child_action_type
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out

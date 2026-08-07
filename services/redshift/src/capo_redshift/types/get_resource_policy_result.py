"""Generated from Smithy shape ``com.amazonaws.redshift#GetResourcePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.resource_policy


class GetResourcePolicyResult(TypedDict, closed=True):
    resource_policy: NotRequired["capo_redshift.types.resource_policy.ResourcePolicy"]
    """<p>The content of the resource policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetResourcePolicyResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_policy" in value:
        import capo_redshift.types.resource_policy

        capo_redshift.types.resource_policy.serialize_query(
            value["resource_policy"], pairs, f"{key_prefix}ResourcePolicy"
        )


def deserialize_query(el: Element) -> GetResourcePolicyResult:
    out: GetResourcePolicyResult = {}  # type: ignore[typeddict-item]
    child_resource_policy = el.find("ResourcePolicy")
    if child_resource_policy is not None:
        import capo_redshift.types.resource_policy

        out["resource_policy"] = capo_redshift.types.resource_policy.deserialize_query(
            child_resource_policy
        )
    return out

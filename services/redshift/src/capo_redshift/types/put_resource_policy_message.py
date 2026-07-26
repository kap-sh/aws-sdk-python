"""Generated from Smithy shape ``com.amazonaws.redshift#PutResourcePolicyMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class PutResourcePolicyMessage(TypedDict, closed=True):
    resource_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource of which its resource policy is updated.</p>"""
    policy: NotRequired["capo_redshift.types.string.String"]
    """<p>The content of the resource policy being updated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutResourcePolicyMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "policy" in value:
        pairs.append((f"{prefix}.Policy", str(value["policy"])))


def deserialize_query(el: Element) -> PutResourcePolicyMessage:
    out: PutResourcePolicyMessage = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.iam#AttachedPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.policy_name_type


class AttachedPolicy(TypedDict, closed=True):
    policy_name: NotRequired["capo_iam.types.policy_name_type.policyNameType"]
    """<p>The friendly name of the attached policy.</p>"""
    policy_arn: NotRequired["capo_iam.types.arn_type.arnType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachedPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_name" in value:
        pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    if "policy_arn" in value:
        pairs.append((f"{key_prefix}PolicyArn", str(value["policy_arn"])))


def deserialize_query(el: Element) -> AttachedPolicy:
    out: AttachedPolicy = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    return out

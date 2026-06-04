"""Generated from Smithy shape ``com.amazonaws.iam#AttachedPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.policy_name_type


class AttachedPolicy(TypedDict):
    policy_name: NotRequired["aws_sdk_iam.types.policy_name_type.policyNameType"]
    """<p>The friendly name of the attached policy.</p>"""
    policy_arn: NotRequired["aws_sdk_iam.types.arn_type.arnType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachedPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "policy_arn" in value:
        pairs.append((f"{prefix}.PolicyArn", str(value["policy_arn"])))


def deserialize_query(el: Element) -> AttachedPolicy:
    out: AttachedPolicy = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.iam#SimulationPolicyListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_document_type

SimulationPolicyListType: TypeAlias = list[
    "capo_iam.types.policy_document_type.policyDocumentType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SimulationPolicyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> SimulationPolicyListType:
    out: SimulationPolicyListType = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SimulationPolicyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SimulationPolicyListType:
    out: SimulationPolicyListType = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out

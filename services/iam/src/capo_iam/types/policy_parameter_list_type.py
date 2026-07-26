"""Generated from Smithy shape ``com.amazonaws.iam#policyParameterListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_parameter

policyParameterListType: TypeAlias = list[
    "capo_iam.types.policy_parameter.PolicyParameter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: policyParameterListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_parameter

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_parameter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> policyParameterListType:
    import capo_iam.types.policy_parameter

    out: policyParameterListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.policy_parameter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: policyParameterListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_parameter

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_parameter.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> policyParameterListType:
    import capo_iam.types.policy_parameter

    out: policyParameterListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.policy_parameter.deserialize_query(child))
    return out

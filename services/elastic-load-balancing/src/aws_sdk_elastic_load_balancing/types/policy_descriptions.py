"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.policy_description

PolicyDescriptions: TypeAlias = list[
    "aws_sdk_elastic_load_balancing.types.policy_description.PolicyDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing.types.policy_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing.types.policy_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyDescriptions:
    import aws_sdk_elastic_load_balancing.types.policy_description

    out: PolicyDescriptions = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing.types.policy_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PolicyDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing.types.policy_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing.types.policy_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PolicyDescriptions:
    import aws_sdk_elastic_load_balancing.types.policy_description

    out: PolicyDescriptions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing.types.policy_description.deserialize_query(
                child
            )
        )
    return out

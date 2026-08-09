"""Generated from Smithy shape ``com.amazonaws.ec2#ThroughResourcesStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.through_resources_statement

ThroughResourcesStatementList: TypeAlias = list[
    "capo_ec2.types.through_resources_statement.ThroughResourcesStatement"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ThroughResourcesStatementList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.through_resources_statement

        capo_ec2.types.through_resources_statement.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ThroughResourcesStatementList:
    import capo_ec2.types.through_resources_statement

    out: ThroughResourcesStatementList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.through_resources_statement.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ThroughResourcesStatementList:
    import capo_ec2.types.through_resources_statement

    out: ThroughResourcesStatementList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.through_resources_statement.deserialize_ec2_query(child)
        )
    return out

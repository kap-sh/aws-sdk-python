"""Generated from Smithy shape ``com.amazonaws.ec2#ThroughResourcesStatementRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.through_resources_statement_request

ThroughResourcesStatementRequestList: TypeAlias = list[
    "capo_ec2.types.through_resources_statement_request.ThroughResourcesStatementRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ThroughResourcesStatementRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.through_resources_statement_request

        capo_ec2.types.through_resources_statement_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ThroughResourcesStatementRequestList:
    import capo_ec2.types.through_resources_statement_request

    out: ThroughResourcesStatementRequestList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.through_resources_statement_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ThroughResourcesStatementRequestList:
    import capo_ec2.types.through_resources_statement_request

    out: ThroughResourcesStatementRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.through_resources_statement_request.deserialize_ec2_query(
                child
            )
        )
    return out

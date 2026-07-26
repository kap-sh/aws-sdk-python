"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_access_scope

NetworkInsightsAccessScopeList: TypeAlias = list[
    "capo_ec2.types.network_insights_access_scope.NetworkInsightsAccessScope"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAccessScopeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.network_insights_access_scope

        capo_ec2.types.network_insights_access_scope.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NetworkInsightsAccessScopeList:
    import capo_ec2.types.network_insights_access_scope

    out: NetworkInsightsAccessScopeList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.network_insights_access_scope.deserialize_ec2_query(child)
        )
    return out

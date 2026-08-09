"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopeAnalysisFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.access_scope_analysis_finding

AccessScopeAnalysisFindingList: TypeAlias = list[
    "capo_ec2.types.access_scope_analysis_finding.AccessScopeAnalysisFinding"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopeAnalysisFindingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.access_scope_analysis_finding

        capo_ec2.types.access_scope_analysis_finding.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AccessScopeAnalysisFindingList:
    import capo_ec2.types.access_scope_analysis_finding

    out: AccessScopeAnalysisFindingList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.access_scope_analysis_finding.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> AccessScopeAnalysisFindingList:
    import capo_ec2.types.access_scope_analysis_finding

    out: AccessScopeAnalysisFindingList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.access_scope_analysis_finding.deserialize_ec2_query(child)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopeAnalysisFindingList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_analysis_finding

AccessScopeAnalysisFindingList: TypeAlias = list[
    "aws_sdk_ec2.types.access_scope_analysis_finding.AccessScopeAnalysisFinding"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopeAnalysisFindingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.access_scope_analysis_finding

        aws_sdk_ec2.types.access_scope_analysis_finding.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AccessScopeAnalysisFindingList:
    import aws_sdk_ec2.types.access_scope_analysis_finding

    out: AccessScopeAnalysisFindingList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.access_scope_analysis_finding.deserialize_ec2_query(child)
        )
    return out

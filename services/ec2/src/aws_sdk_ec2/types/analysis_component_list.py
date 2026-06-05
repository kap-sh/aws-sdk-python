"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisComponentList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_component

AnalysisComponentList: TypeAlias = list[
    "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisComponentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.analysis_component

        aws_sdk_ec2.types.analysis_component.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AnalysisComponentList:
    import aws_sdk_ec2.types.analysis_component

    out: AnalysisComponentList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.analysis_component.deserialize_ec2_query(child))
    return out

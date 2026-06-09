"""Generated from Smithy shape ``com.amazonaws.ec2#DeclarativePoliciesReportList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.declarative_policies_report

DeclarativePoliciesReportList: TypeAlias = list[
    "aws_sdk_ec2.types.declarative_policies_report.DeclarativePoliciesReport"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeclarativePoliciesReportList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.declarative_policies_report

        aws_sdk_ec2.types.declarative_policies_report.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> DeclarativePoliciesReportList:
    import aws_sdk_ec2.types.declarative_policies_report

    out: DeclarativePoliciesReportList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.declarative_policies_report.deserialize_ec2_query(child)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#ReasonCodesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.report_instance_reason_codes

ReasonCodesList: TypeAlias = list[
    "aws_sdk_ec2.types.report_instance_reason_codes.ReportInstanceReasonCodes"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReasonCodesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.report_instance_reason_codes

        aws_sdk_ec2.types.report_instance_reason_codes.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ReasonCodesList:
    import aws_sdk_ec2.types.report_instance_reason_codes

    out: ReasonCodesList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.report_instance_reason_codes.deserialize_ec2_query(child)
        )
    return out

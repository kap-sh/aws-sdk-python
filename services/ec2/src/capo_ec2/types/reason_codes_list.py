"""Generated from Smithy shape ``com.amazonaws.ec2#ReasonCodesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.report_instance_reason_codes

ReasonCodesList: TypeAlias = list[
    "capo_ec2.types.report_instance_reason_codes.ReportInstanceReasonCodes"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReasonCodesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.report_instance_reason_codes

        capo_ec2.types.report_instance_reason_codes.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReasonCodesList:
    import capo_ec2.types.report_instance_reason_codes

    out: ReasonCodesList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.report_instance_reason_codes.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ReasonCodesList:
    import capo_ec2.types.report_instance_reason_codes

    out: ReasonCodesList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.report_instance_reason_codes.deserialize_ec2_query(child)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#EbsStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ebs_status_details

EbsStatusDetailsList: TypeAlias = list[
    "capo_ec2.types.ebs_status_details.EbsStatusDetails"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsStatusDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ebs_status_details

        capo_ec2.types.ebs_status_details.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> EbsStatusDetailsList:
    import capo_ec2.types.ebs_status_details

    out: EbsStatusDetailsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ebs_status_details.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> EbsStatusDetailsList:
    import capo_ec2.types.ebs_status_details

    out: EbsStatusDetailsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ebs_status_details.deserialize_ec2_query(child))
    return out

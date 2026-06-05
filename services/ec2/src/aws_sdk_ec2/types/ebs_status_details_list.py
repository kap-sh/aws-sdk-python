"""Generated from Smithy shape ``com.amazonaws.ec2#EbsStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_status_details

EbsStatusDetailsList: TypeAlias = list[
    "aws_sdk_ec2.types.ebs_status_details.EbsStatusDetails"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsStatusDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ebs_status_details

        aws_sdk_ec2.types.ebs_status_details.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> EbsStatusDetailsList:
    import aws_sdk_ec2.types.ebs_status_details

    out: EbsStatusDetailsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ebs_status_details.deserialize_ec2_query(child))
    return out

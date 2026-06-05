"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1DHGroupNumbersRequestList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value

Phase1DHGroupNumbersRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value.Phase1DHGroupNumbersRequestListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase1DHGroupNumbersRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value

        aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> Phase1DHGroupNumbersRequestList:
    import aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value

    out: Phase1DHGroupNumbersRequestList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.phase1_dh_group_numbers_request_list_value.deserialize_ec2_query(
                child
            )
        )
    return out

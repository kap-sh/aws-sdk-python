"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIdentityIdFormatResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.id_format_list


class DescribeIdentityIdFormatResult(TypedDict):
    statuses: NotRequired["aws_sdk_ec2.types.id_format_list.IdFormatList"]
    """<p>Information about the ID format for the resources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIdentityIdFormatResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "statuses" in value:
        import aws_sdk_ec2.types.id_format_list

        aws_sdk_ec2.types.id_format_list.serialize_ec2_query(
            value["statuses"], pairs, f"{prefix}.StatusSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeIdentityIdFormatResult:
    out: DescribeIdentityIdFormatResult = {}  # type: ignore[typeddict-item]
    if el.find("StatusSet") is not None:
        import aws_sdk_ec2.types.id_format_list

        out["statuses"] = aws_sdk_ec2.types.id_format_list.deserialize_ec2_query(
            el, "StatusSet"
        )
    return out

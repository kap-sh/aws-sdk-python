"""Generated from Smithy shape ``com.amazonaws.ec2#PrincipalIdFormat``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.id_format_list
    import aws_sdk_ec2.types.string


class PrincipalIdFormat(TypedDict):
    arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>PrincipalIdFormatARN description</p>"""
    statuses: NotRequired["aws_sdk_ec2.types.id_format_list.IdFormatList"]
    """<p>PrincipalIdFormatStatuses description</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrincipalIdFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "statuses" in value:
        import aws_sdk_ec2.types.id_format_list

        aws_sdk_ec2.types.id_format_list.serialize_ec2_query(
            value["statuses"], pairs, f"{prefix}.StatusSet"
        )


def deserialize_ec2_query(el: Element) -> PrincipalIdFormat:
    out: PrincipalIdFormat = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    if el.find("StatusSet") is not None:
        import aws_sdk_ec2.types.id_format_list

        out["statuses"] = aws_sdk_ec2.types.id_format_list.deserialize_ec2_query(
            el, "StatusSet"
        )
    return out

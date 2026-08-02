"""Generated from Smithy shape ``com.amazonaws.ec2#PrincipalIdFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.id_format_list
    import capo_ec2.types.string


class PrincipalIdFormat(TypedDict, closed=True):
    arn: NotRequired["capo_ec2.types.string.String"]
    """<p>PrincipalIdFormatARN description</p>"""
    statuses: NotRequired["capo_ec2.types.id_format_list.IdFormatList"]
    """<p>PrincipalIdFormatStatuses description</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrincipalIdFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "statuses" in value:
        import capo_ec2.types.id_format_list

        capo_ec2.types.id_format_list.serialize_ec2_query(
            value["statuses"], pairs, f"{key_prefix}StatusSet"
        )


def deserialize_ec2_query(el: Element) -> PrincipalIdFormat:
    out: PrincipalIdFormat = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    if el.find("StatusSet") is not None:
        import capo_ec2.types.id_format_list

        out["statuses"] = capo_ec2.types.id_format_list.deserialize_ec2_query(
            el, "StatusSet"
        )
    return out

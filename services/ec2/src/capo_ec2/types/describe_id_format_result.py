"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIdFormatResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.id_format_list


class DescribeIdFormatResult(TypedDict, closed=True):
    statuses: NotRequired["capo_ec2.types.id_format_list.IdFormatList"]
    """<p>Information about the ID format for the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIdFormatResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "statuses" in value:
        import capo_ec2.types.id_format_list

        capo_ec2.types.id_format_list.serialize_ec2_query(
            value["statuses"], pairs, f"{key_prefix}StatusSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeIdFormatResult:
    out: DescribeIdFormatResult = {}  # type: ignore[typeddict-item]
    if el.find("StatusSet") is not None:
        import capo_ec2.types.id_format_list

        out["statuses"] = capo_ec2.types.id_format_list.deserialize_ec2_query(
            el, "StatusSet"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAggregateIdFormatResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.id_format_list


class DescribeAggregateIdFormatResult(TypedDict, closed=True):
    use_long_ids_aggregated: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether all resource types in the Region are configured to use longer IDs. This value is only <code>true</code> if all users are configured to use longer IDs for all resources types in the Region.</p>"""
    statuses: NotRequired["capo_ec2.types.id_format_list.IdFormatList"]
    """<p>Information about each resource's ID format.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAggregateIdFormatResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "use_long_ids_aggregated" in value:
        pairs.append(
            (
                f"{key_prefix}UseLongIdsAggregated",
                "true" if value["use_long_ids_aggregated"] else "false",
            )
        )
    if "statuses" in value:
        import capo_ec2.types.id_format_list

        capo_ec2.types.id_format_list.serialize_ec2_query(
            value["statuses"], pairs, f"{key_prefix}StatusSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeAggregateIdFormatResult:
    out: DescribeAggregateIdFormatResult = {}  # type: ignore[typeddict-item]
    child_use_long_ids_aggregated = el.find("UseLongIdsAggregated")
    if child_use_long_ids_aggregated is not None:
        out["use_long_ids_aggregated"] = (
            child_use_long_ids_aggregated.text or ""
        ).lower() == "true"
    if el.find("StatusSet") is not None:
        import capo_ec2.types.id_format_list

        out["statuses"] = capo_ec2.types.id_format_list.deserialize_ec2_query(
            el, "StatusSet"
        )
    return out

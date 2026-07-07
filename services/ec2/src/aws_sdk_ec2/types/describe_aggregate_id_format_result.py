"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAggregateIdFormatResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.id_format_list


class DescribeAggregateIdFormatResult(TypedDict, closed=True):
    use_long_ids_aggregated: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether all resource types in the Region are configured to use longer IDs. This value is only <code>true</code> if all users are configured to use longer IDs for all resources types in the Region.</p>"""
    statuses: NotRequired["aws_sdk_ec2.types.id_format_list.IdFormatList"]
    """<p>Information about each resource's ID format.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAggregateIdFormatResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "use_long_ids_aggregated" in value:
        pairs.append(
            (
                f"{prefix}.UseLongIdsAggregated",
                "true" if value["use_long_ids_aggregated"] else "false",
            )
        )
    if "statuses" in value:
        import aws_sdk_ec2.types.id_format_list

        aws_sdk_ec2.types.id_format_list.serialize_ec2_query(
            value["statuses"], pairs, f"{prefix}.StatusSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeAggregateIdFormatResult:
    out: DescribeAggregateIdFormatResult = {}  # type: ignore[typeddict-item]
    child_use_long_ids_aggregated = el.find("UseLongIdsAggregated")
    if child_use_long_ids_aggregated is not None:
        out["use_long_ids_aggregated"] = (
            child_use_long_ids_aggregated.text or ""
        ).lower() == "true"
    if el.find("StatusSet") is not None:
        import aws_sdk_ec2.types.id_format_list

        out["statuses"] = aws_sdk_ec2.types.id_format_list.deserialize_ec2_query(
            el, "StatusSet"
        )
    return out

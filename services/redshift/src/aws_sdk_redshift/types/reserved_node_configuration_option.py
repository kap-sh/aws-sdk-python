"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeConfigurationOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer
    import aws_sdk_redshift.types.reserved_node
    import aws_sdk_redshift.types.reserved_node_offering


class ReservedNodeConfigurationOption(TypedDict):
    source_reserved_node: NotRequired[
        "aws_sdk_redshift.types.reserved_node.ReservedNode"
    ]
    target_reserved_node_count: NotRequired["aws_sdk_redshift.types.integer.Integer"]
    """<p>The target reserved-node count.</p>"""
    target_reserved_node_offering: NotRequired[
        "aws_sdk_redshift.types.reserved_node_offering.ReservedNodeOffering"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeConfigurationOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_reserved_node" in value:
        import aws_sdk_redshift.types.reserved_node

        aws_sdk_redshift.types.reserved_node.serialize_query(
            value["source_reserved_node"], pairs, f"{prefix}.SourceReservedNode"
        )
    if "target_reserved_node_count" in value:
        pairs.append(
            (
                f"{prefix}.TargetReservedNodeCount",
                str(value["target_reserved_node_count"]),
            )
        )
    if "target_reserved_node_offering" in value:
        import aws_sdk_redshift.types.reserved_node_offering

        aws_sdk_redshift.types.reserved_node_offering.serialize_query(
            value["target_reserved_node_offering"],
            pairs,
            f"{prefix}.TargetReservedNodeOffering",
        )


def deserialize_query(el: Element) -> ReservedNodeConfigurationOption:
    out: ReservedNodeConfigurationOption = {}  # type: ignore[typeddict-item]
    child_source_reserved_node = el.find("SourceReservedNode")
    if child_source_reserved_node is not None:
        import aws_sdk_redshift.types.reserved_node

        out["source_reserved_node"] = (
            aws_sdk_redshift.types.reserved_node.deserialize_query(
                child_source_reserved_node
            )
        )
    child_target_reserved_node_count = el.find("TargetReservedNodeCount")
    if child_target_reserved_node_count is not None:
        out["target_reserved_node_count"] = int(
            child_target_reserved_node_count.text or ""
        )
    child_target_reserved_node_offering = el.find("TargetReservedNodeOffering")
    if child_target_reserved_node_offering is not None:
        import aws_sdk_redshift.types.reserved_node_offering

        out["target_reserved_node_offering"] = (
            aws_sdk_redshift.types.reserved_node_offering.deserialize_query(
                child_target_reserved_node_offering
            )
        )
    return out

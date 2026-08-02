"""Generated from Smithy shape ``com.amazonaws.ec2#DestinationOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.destination_file_format


class DestinationOptionsRequest(TypedDict, closed=True):
    file_format: NotRequired[
        "capo_ec2.types.destination_file_format.DestinationFileFormat"
    ]
    """<p>The format for the flow log. The default is <code>plain-text</code>.</p>"""
    hive_compatible_partitions: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3. The default is <code>false</code>.</p>"""
    per_hour_partition: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to partition the flow log per hour. This reduces the cost and response time for queries. The default is <code>false</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DestinationOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "file_format" in value:
        import capo_ec2.types.destination_file_format

        capo_ec2.types.destination_file_format.serialize_ec2_query(
            value["file_format"], pairs, f"{key_prefix}FileFormat"
        )
    if "hive_compatible_partitions" in value:
        pairs.append(
            (
                f"{key_prefix}HiveCompatiblePartitions",
                "true" if value["hive_compatible_partitions"] else "false",
            )
        )
    if "per_hour_partition" in value:
        pairs.append(
            (
                f"{key_prefix}PerHourPartition",
                "true" if value["per_hour_partition"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DestinationOptionsRequest:
    out: DestinationOptionsRequest = {}  # type: ignore[typeddict-item]
    child_file_format = el.find("FileFormat")
    if child_file_format is not None:
        import capo_ec2.types.destination_file_format

        out["file_format"] = (
            capo_ec2.types.destination_file_format.deserialize_ec2_query(
                child_file_format
            )
        )
    child_hive_compatible_partitions = el.find("HiveCompatiblePartitions")
    if child_hive_compatible_partitions is not None:
        out["hive_compatible_partitions"] = (
            child_hive_compatible_partitions.text or ""
        ).lower() == "true"
    child_per_hour_partition = el.find("PerHourPartition")
    if child_per_hour_partition is not None:
        out["per_hour_partition"] = (
            child_per_hour_partition.text or ""
        ).lower() == "true"
    return out

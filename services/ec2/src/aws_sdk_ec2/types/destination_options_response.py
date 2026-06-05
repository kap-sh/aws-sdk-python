"""Generated from Smithy shape ``com.amazonaws.ec2#DestinationOptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.destination_file_format


class DestinationOptionsResponse(TypedDict):
    file_format: NotRequired[
        "aws_sdk_ec2.types.destination_file_format.DestinationFileFormat"
    ]
    """<p>The format for the flow log.</p>"""
    hive_compatible_partitions: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3.</p>"""
    per_hour_partition: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to partition the flow log per hour.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DestinationOptionsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "file_format" in value:
        import aws_sdk_ec2.types.destination_file_format

        aws_sdk_ec2.types.destination_file_format.serialize_ec2_query(
            value["file_format"], pairs, f"{prefix}.FileFormat"
        )
    if "hive_compatible_partitions" in value:
        pairs.append(
            (
                f"{prefix}.HiveCompatiblePartitions",
                "true" if value["hive_compatible_partitions"] else "false",
            )
        )
    if "per_hour_partition" in value:
        pairs.append(
            (
                f"{prefix}.PerHourPartition",
                "true" if value["per_hour_partition"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DestinationOptionsResponse:
    out: DestinationOptionsResponse = {}  # type: ignore[typeddict-item]
    child_file_format = el.find("FileFormat")
    if child_file_format is not None:
        import aws_sdk_ec2.types.destination_file_format

        out["file_format"] = (
            aws_sdk_ec2.types.destination_file_format.deserialize_ec2_query(
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

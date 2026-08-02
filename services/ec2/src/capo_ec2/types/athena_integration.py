"""Generated from Smithy shape ``com.amazonaws.ec2#AthenaIntegration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.partition_load_frequency
    import capo_ec2.types.string


class AthenaIntegration(TypedDict, closed=True):
    integration_result_s3_destination_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The location in Amazon S3 to store the generated CloudFormation template.</p>"""
    partition_load_frequency: NotRequired[
        "capo_ec2.types.partition_load_frequency.PartitionLoadFrequency"
    ]
    """<p>The schedule for adding new partitions to the table.</p>"""
    partition_start_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date for the partition.</p>"""
    partition_end_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The end date for the partition.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AthenaIntegration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "integration_result_s3_destination_arn" in value:
        pairs.append(
            (
                f"{key_prefix}IntegrationResultS3DestinationArn",
                str(value["integration_result_s3_destination_arn"]),
            )
        )
    if "partition_load_frequency" in value:
        import capo_ec2.types.partition_load_frequency

        capo_ec2.types.partition_load_frequency.serialize_ec2_query(
            value["partition_load_frequency"],
            pairs,
            f"{key_prefix}PartitionLoadFrequency",
        )
    if "partition_start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["partition_start_date"], pairs, f"{key_prefix}PartitionStartDate"
        )
    if "partition_end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["partition_end_date"], pairs, f"{key_prefix}PartitionEndDate"
        )


def deserialize_ec2_query(el: Element) -> AthenaIntegration:
    out: AthenaIntegration = {}  # type: ignore[typeddict-item]
    child_integration_result_s3_destination_arn = el.find(
        "IntegrationResultS3DestinationArn"
    )
    if child_integration_result_s3_destination_arn is not None:
        out["integration_result_s3_destination_arn"] = str(
            child_integration_result_s3_destination_arn.text or ""
        )
    child_partition_load_frequency = el.find("PartitionLoadFrequency")
    if child_partition_load_frequency is not None:
        import capo_ec2.types.partition_load_frequency

        out["partition_load_frequency"] = (
            capo_ec2.types.partition_load_frequency.deserialize_ec2_query(
                child_partition_load_frequency
            )
        )
    child_partition_start_date = el.find("PartitionStartDate")
    if child_partition_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["partition_start_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_partition_start_date
            )
        )
    child_partition_end_date = el.find("PartitionEndDate")
    if child_partition_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["partition_end_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_partition_end_date
            )
        )
    return out

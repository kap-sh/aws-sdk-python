"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dataset_status
    import aws_sdk_comprehend.types.dataset_type
    import aws_sdk_comprehend.types.timestamp


class DatasetFilter(TypedDict, closed=True):
    status: NotRequired["aws_sdk_comprehend.types.dataset_status.DatasetStatus"]
    """<p>Filter the datasets based on the dataset status.</p>"""
    dataset_type: NotRequired["aws_sdk_comprehend.types.dataset_type.DatasetType"]
    """<p>Filter the datasets based on the dataset type.</p>"""
    creation_time_after: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the datasets to include datasets created after the specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the datasets to include datasets created before the specified time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_comprehend.types.dataset_status

        out["Status"] = aws_sdk_comprehend.types.dataset_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "dataset_type" in value:
        import aws_sdk_comprehend.types.dataset_type

        out["DatasetType"] = (
            aws_sdk_comprehend.types.dataset_type.serialize_aws_json_1_1(
                value["dataset_type"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetFilter:
    out: DatasetFilter = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_comprehend.types.dataset_status

        out["status"] = (
            aws_sdk_comprehend.types.dataset_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "DatasetType" in data:
        import aws_sdk_comprehend.types.dataset_type

        out["dataset_type"] = (
            aws_sdk_comprehend.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    if "CreationTimeAfter" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    return out

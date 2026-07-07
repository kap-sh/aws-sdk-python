"""Generated from Smithy shape ``com.amazonaws.glue#PartitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.parameters_map
    import aws_sdk_glue.types.storage_descriptor
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.value_string_list


class PartitionInput(TypedDict, closed=True):
    values: NotRequired["aws_sdk_glue.types.value_string_list.ValueStringList"]
    """<p>The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.</p> <p>The values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise Glue will add the values to the wrong keys.</p>"""
    last_access_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The last time at which the partition was accessed.</p>"""
    storage_descriptor: NotRequired[
        "aws_sdk_glue.types.storage_descriptor.StorageDescriptor"
    ]
    """<p>Provides information about the physical location where the partition is stored.</p>"""
    parameters: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define partition parameters.</p>"""
    last_analyzed_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The last time at which column statistics were computed for this partition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionInput) -> dict:
    out: dict = {}
    if "values" in value:
        import aws_sdk_glue.types.value_string_list

        out["Values"] = aws_sdk_glue.types.value_string_list.serialize_aws_json_1_1(
            value["values"]
        )
    if "last_access_time" in value:
        import aws_sdk_glue.types.timestamp

        out["LastAccessTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_access_time"]
        )
    if "storage_descriptor" in value:
        import aws_sdk_glue.types.storage_descriptor

        out["StorageDescriptor"] = (
            aws_sdk_glue.types.storage_descriptor.serialize_aws_json_1_1(
                value["storage_descriptor"]
            )
        )
    if "parameters" in value:
        import aws_sdk_glue.types.parameters_map

        out["Parameters"] = aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "last_analyzed_time" in value:
        import aws_sdk_glue.types.timestamp

        out["LastAnalyzedTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_analyzed_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionInput:
    out: PartitionInput = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_glue.types.value_string_list

        out["values"] = aws_sdk_glue.types.value_string_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    if "LastAccessTime" in data:
        import aws_sdk_glue.types.timestamp

        out["last_access_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastAccessTime"]
        )
    if "StorageDescriptor" in data:
        import aws_sdk_glue.types.storage_descriptor

        out["storage_descriptor"] = (
            aws_sdk_glue.types.storage_descriptor.deserialize_aws_json_1_1(
                data["StorageDescriptor"]
            )
        )
    if "Parameters" in data:
        import aws_sdk_glue.types.parameters_map

        out["parameters"] = aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "LastAnalyzedTime" in data:
        import aws_sdk_glue.types.timestamp

        out["last_analyzed_time"] = (
            aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
                data["LastAnalyzedTime"]
            )
        )
    return out

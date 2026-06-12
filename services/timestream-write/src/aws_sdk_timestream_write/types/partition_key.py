"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#PartitionKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.partition_key_enforcement_level
    import aws_sdk_timestream_write.types.partition_key_type
    import aws_sdk_timestream_write.types.schema_name


class PartitionKey(TypedDict):
    type: "aws_sdk_timestream_write.types.partition_key_type.PartitionKeyType"
    """<p> The type of the partition key. Options are DIMENSION (dimension key) and MEASURE (measure key). </p>"""
    name: NotRequired["aws_sdk_timestream_write.types.schema_name.SchemaName"]
    """<p> The name of the attribute used for a dimension key. </p>"""
    enforcement_in_record: NotRequired[
        "aws_sdk_timestream_write.types.partition_key_enforcement_level.PartitionKeyEnforcementLevel"
    ]
    """<p> The level of enforcement for the specification of a dimension key in ingested records. Options are REQUIRED (dimension key must be specified) and OPTIONAL (dimension key does not have to be specified). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKey) -> dict:
    out: dict = {}
    import aws_sdk_timestream_write.types.partition_key_type

    out["Type"] = (
        aws_sdk_timestream_write.types.partition_key_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    if "name" in value:
        out["Name"] = value["name"]
    if "enforcement_in_record" in value:
        import aws_sdk_timestream_write.types.partition_key_enforcement_level

        out["EnforcementInRecord"] = (
            aws_sdk_timestream_write.types.partition_key_enforcement_level.serialize_aws_json_1_0(
                value["enforcement_in_record"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PartitionKey:
    out: PartitionKey = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_timestream_write.types.partition_key_type

        out["type"] = (
            aws_sdk_timestream_write.types.partition_key_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("PartitionKey.type required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "EnforcementInRecord" in data:
        import aws_sdk_timestream_write.types.partition_key_enforcement_level

        out["enforcement_in_record"] = (
            aws_sdk_timestream_write.types.partition_key_enforcement_level.deserialize_aws_json_1_0(
                data["EnforcementInRecord"]
            )
        )
    return out

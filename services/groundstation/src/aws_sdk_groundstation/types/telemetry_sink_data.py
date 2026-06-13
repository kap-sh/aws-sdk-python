"""Generated from Smithy shape ``com.amazonaws.groundstation#TelemetrySinkData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.kinesis_data_stream_data


class _TelemetrySinkData_kinesisDataStreamData(TypedDict):
    kinesisDataStreamData: (
        "aws_sdk_groundstation.types.kinesis_data_stream_data.KinesisDataStreamData"
    )


TelemetrySinkData: TypeAlias = _TelemetrySinkData_kinesisDataStreamData


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySinkData) -> dict:
    if "kinesisDataStreamData" in value:
        import aws_sdk_groundstation.types.kinesis_data_stream_data

        return {
            "kinesisDataStreamData": aws_sdk_groundstation.types.kinesis_data_stream_data.serialize_json(
                value["kinesisDataStreamData"]
            )
        }
    else:
        raise SerializationError("TelemetrySinkData: no variant present")


def deserialize_json(data: dict) -> TelemetrySinkData:
    if "kinesisDataStreamData" in data:
        import aws_sdk_groundstation.types.kinesis_data_stream_data

        return {
            "kinesisDataStreamData": aws_sdk_groundstation.types.kinesis_data_stream_data.deserialize_json(
                data["kinesisDataStreamData"]
            )
        }
    else:
        raise DeserializationError("TelemetrySinkData: no recognized variant key")

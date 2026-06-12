"""Generated from Smithy shape ``com.amazonaws.healthlake#PreloadDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.preload_data_type


class PreloadDataConfig(TypedDict):
    preload_data_type: "aws_sdk_healthlake.types.preload_data_type.PreloadDataType"
    """<p>The type of preloaded data. Only Synthea preloaded data is supported.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreloadDataConfig) -> dict:
    out: dict = {}
    import aws_sdk_healthlake.types.preload_data_type

    out["PreloadDataType"] = (
        aws_sdk_healthlake.types.preload_data_type.serialize_aws_json_1_0(
            value["preload_data_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PreloadDataConfig:
    out: PreloadDataConfig = {}  # type: ignore[typeddict-item]
    if "PreloadDataType" in data:
        import aws_sdk_healthlake.types.preload_data_type

        out["preload_data_type"] = (
            aws_sdk_healthlake.types.preload_data_type.deserialize_aws_json_1_0(
                data["PreloadDataType"]
            )
        )
    else:
        raise DeserializationError("PreloadDataConfig.preload_data_type required")
    return out

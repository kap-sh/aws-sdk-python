"""Generated from Smithy shape ``com.amazonaws.healthlake#PreloadDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.preload_data_type


class PreloadDataConfig(TypedDict, closed=True):
    preload_data_type: "capo_healthlake.types.preload_data_type.PreloadDataType"
    """<p>The type of preloaded data. Only Synthea preloaded data is supported.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreloadDataConfig) -> dict:
    out: dict = {}
    import capo_healthlake.types.preload_data_type

    out["PreloadDataType"] = (
        capo_healthlake.types.preload_data_type.serialize_aws_json_1_0(
            value["preload_data_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PreloadDataConfig:
    out: PreloadDataConfig = {}  # type: ignore[typeddict-item]
    if "PreloadDataType" in data:
        import capo_healthlake.types.preload_data_type

        out["preload_data_type"] = (
            capo_healthlake.types.preload_data_type.deserialize_aws_json_1_0(
                data["PreloadDataType"]
            )
        )
    else:
        raise DeserializationError("PreloadDataConfig.preload_data_type required")
    return out

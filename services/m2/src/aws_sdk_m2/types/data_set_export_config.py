"""Generated from Smithy shape ``com.amazonaws.m2#DataSetExportConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_export_list


class _DataSetExportConfig_s3Location(TypedDict):
    s3Location: "str"


class _DataSetExportConfig_dataSets(TypedDict):
    dataSets: "aws_sdk_m2.types.data_set_export_list.DataSetExportList"


DataSetExportConfig: TypeAlias = (
    _DataSetExportConfig_s3Location | _DataSetExportConfig_dataSets
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSetExportConfig) -> dict:
    if "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    elif "dataSets" in value:
        import aws_sdk_m2.types.data_set_export_list

        return {
            "dataSets": aws_sdk_m2.types.data_set_export_list.serialize_json(
                value["dataSets"]
            )
        }
    else:
        raise SerializationError("DataSetExportConfig: no variant present")


def deserialize_json(data: dict) -> DataSetExportConfig:
    if "s3Location" in data:
        return {"s3Location": data["s3Location"]}
    elif "dataSets" in data:
        import aws_sdk_m2.types.data_set_export_list

        return {
            "dataSets": aws_sdk_m2.types.data_set_export_list.deserialize_json(
                data["dataSets"]
            )
        }
    else:
        raise DeserializationError("DataSetExportConfig: no recognized variant key")

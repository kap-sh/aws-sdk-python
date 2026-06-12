"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_import_list
    import aws_sdk_m2.types.string2000


class _DataSetImportConfig_s3Location(TypedDict):
    s3Location: "aws_sdk_m2.types.string2000.String2000"


class _DataSetImportConfig_dataSets(TypedDict):
    dataSets: "aws_sdk_m2.types.data_set_import_list.DataSetImportList"


DataSetImportConfig: TypeAlias = (
    _DataSetImportConfig_s3Location | _DataSetImportConfig_dataSets
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportConfig) -> dict:
    if "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    elif "dataSets" in value:
        import aws_sdk_m2.types.data_set_import_list

        return {
            "dataSets": aws_sdk_m2.types.data_set_import_list.serialize_json(
                value["dataSets"]
            )
        }
    else:
        raise SerializationError("DataSetImportConfig: no variant present")


def deserialize_json(data: dict) -> DataSetImportConfig:
    if "s3Location" in data:
        return {"s3Location": data["s3Location"]}
    elif "dataSets" in data:
        import aws_sdk_m2.types.data_set_import_list

        return {
            "dataSets": aws_sdk_m2.types.data_set_import_list.deserialize_json(
                data["dataSets"]
            )
        }
    else:
        raise DeserializationError("DataSetImportConfig: no recognized variant key")

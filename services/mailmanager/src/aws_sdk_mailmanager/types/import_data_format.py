"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportDataFormat``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.import_data_type


class ImportDataFormat(TypedDict):
    import_data_type: "aws_sdk_mailmanager.types.import_data_type.ImportDataType"
    """<p>The type of file that would be passed as an input for the address list import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDataFormat) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.import_data_type

    out["ImportDataType"] = (
        aws_sdk_mailmanager.types.import_data_type.serialize_aws_json_1_0(
            value["import_data_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportDataFormat:
    out: ImportDataFormat = {}  # type: ignore[typeddict-item]
    if "ImportDataType" in data:
        import aws_sdk_mailmanager.types.import_data_type

        out["import_data_type"] = (
            aws_sdk_mailmanager.types.import_data_type.deserialize_aws_json_1_0(
                data["ImportDataType"]
            )
        )
    else:
        raise DeserializationError("ImportDataFormat.import_data_type required")
    return out

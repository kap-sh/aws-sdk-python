"""Generated from Smithy shape ``com.amazonaws.m2#CreateDataSetImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.client_token
    import aws_sdk_m2.types.data_set_import_config
    import aws_sdk_m2.types.identifier


class CreateDataSetImportTaskRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application for which you want to import data sets.</p>"""
    import_config: "aws_sdk_m2.types.data_set_import_config.DataSetImportConfig"
    """<p>The data set import task configuration.</p>"""
    client_token: NotRequired["aws_sdk_m2.types.client_token.ClientToken"]
    """<p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set import. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSetImportTaskRequest) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.data_set_import_config

    out["importConfig"] = aws_sdk_m2.types.data_set_import_config.serialize_json(
        value["import_config"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDataSetImportTaskRequest:
    out: CreateDataSetImportTaskRequest = {}  # type: ignore[typeddict-item]
    if "importConfig" in data:
        import aws_sdk_m2.types.data_set_import_config

        out["import_config"] = aws_sdk_m2.types.data_set_import_config.deserialize_json(
            data["importConfig"]
        )
    else:
        raise DeserializationError(
            "CreateDataSetImportTaskRequest.import_config required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

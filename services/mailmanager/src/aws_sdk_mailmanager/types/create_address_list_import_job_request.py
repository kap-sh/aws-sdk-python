"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddressListImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address_list_id
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.import_data_format
    import aws_sdk_mailmanager.types.job_name


class CreateAddressListImportJobRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId"
    """<p>The unique identifier of the address list for importing addresses to.</p>"""
    name: "aws_sdk_mailmanager.types.job_name.JobName"
    """<p>A user-friendly name for the import job.</p>"""
    import_data_format: "aws_sdk_mailmanager.types.import_data_format.ImportDataFormat"
    """<p>The format of the input for an import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddressListImportJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["AddressListId"] = value["address_list_id"]
    out["Name"] = value["name"]
    import aws_sdk_mailmanager.types.import_data_format

    out["ImportDataFormat"] = (
        aws_sdk_mailmanager.types.import_data_format.serialize_aws_json_1_0(
            value["import_data_format"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddressListImportJobRequest:
    out: CreateAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError(
            "CreateAddressListImportJobRequest.address_list_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAddressListImportJobRequest.name required")
    if "ImportDataFormat" in data:
        import aws_sdk_mailmanager.types.import_data_format

        out["import_data_format"] = (
            aws_sdk_mailmanager.types.import_data_format.deserialize_aws_json_1_0(
                data["ImportDataFormat"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAddressListImportJobRequest.import_data_format required"
        )
    return out

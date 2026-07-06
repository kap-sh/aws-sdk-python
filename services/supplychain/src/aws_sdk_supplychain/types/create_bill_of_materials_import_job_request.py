"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateBillOfMaterialsImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.client_token
    import aws_sdk_supplychain.types.configuration_s3_uri
    import aws_sdk_supplychain.types.uuid


class CreateBillOfMaterialsImportJobRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    s3uri: "aws_sdk_supplychain.types.configuration_s3_uri.ConfigurationS3Uri"
    """<p>The S3 URI of the CSV file to be imported. The bucket must grant permissions for AWS Supply Chain to read the file.</p>"""
    client_token: NotRequired["aws_sdk_supplychain.types.client_token.ClientToken"]
    """<p>An idempotency token ensures the API request is only completed no more than once. This way, retrying the request will not trigger the operation multiple times. A client token is a unique, case-sensitive string of 33 to 128 ASCII characters. To make an idempotent API request, specify a client token in the request. You should not reuse the same client token for other requests. If you retry a successful request with the same client token, the request will succeed with no further actions being taken, and you will receive the same API response as the original successful request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBillOfMaterialsImportJobRequest) -> dict:
    out: dict = {}
    out["s3uri"] = value["s3uri"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateBillOfMaterialsImportJobRequest:
    out: CreateBillOfMaterialsImportJobRequest = {}  # type: ignore[typeddict-item]
    if "s3uri" in data:
        out["s3uri"] = data["s3uri"]
    else:
        raise DeserializationError(
            "CreateBillOfMaterialsImportJobRequest.s3uri required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

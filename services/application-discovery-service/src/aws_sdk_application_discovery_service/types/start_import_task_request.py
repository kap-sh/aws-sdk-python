"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.client_request_token
    import aws_sdk_application_discovery_service.types.import_task_name
    import aws_sdk_application_discovery_service.types.import_url


class StartImportTaskRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_application_discovery_service.types.client_request_token.ClientRequestToken"
    ]
    """<p>Optional. A unique token that you can provide to prevent the same import request from occurring more than once. If you don't provide a token, a token is automatically generated.</p> <p>Sending more than one <code>StartImportTask</code> request with the same client request token will return information about the original import task with that client request token.</p>"""
    name: "aws_sdk_application_discovery_service.types.import_task_name.ImportTaskName"
    """<p>A descriptive name for this request. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.</p>"""
    import_url: "aws_sdk_application_discovery_service.types.import_url.ImportURL"
    """<p>The URL for your import file that you've uploaded to Amazon S3.</p> <note> <p>If you're using the Amazon Web Services CLI, this URL is structured as follows: <code>s3://BucketName/ImportFileName.CSV</code> </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportTaskRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["name"] = value["name"]
    out["importUrl"] = value["import_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportTaskRequest:
    out: StartImportTaskRequest = {}  # type: ignore[typeddict-item]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartImportTaskRequest.name required")
    if "importUrl" in data:
        out["import_url"] = data["importUrl"]
    else:
        raise DeserializationError("StartImportTaskRequest.import_url required")
    return out

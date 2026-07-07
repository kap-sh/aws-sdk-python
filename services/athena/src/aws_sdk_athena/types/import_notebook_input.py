"""Generated from Smithy shape ``com.amazonaws.athena#ImportNotebookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.client_request_token
    import aws_sdk_athena.types.notebook_name
    import aws_sdk_athena.types.notebook_type
    import aws_sdk_athena.types.payload
    import aws_sdk_athena.types.s3_uri
    import aws_sdk_athena.types.work_group_name


class ImportNotebookInput(TypedDict, closed=True):
    work_group: "aws_sdk_athena.types.work_group_name.WorkGroupName"
    """<p>The name of the Spark enabled workgroup to import the notebook to.</p>"""
    name: "aws_sdk_athena.types.notebook_name.NotebookName"
    """<p>The name of the notebook to import.</p>"""
    payload: NotRequired["aws_sdk_athena.types.payload.Payload"]
    """<p>The notebook content to be imported. The payload must be in <code>ipynb</code> format.</p>"""
    type: "aws_sdk_athena.types.notebook_type.NotebookType"
    """<p>The notebook content type. Currently, the only valid type is <code>IPYNB</code>.</p>"""
    notebook_s3_location_uri: NotRequired["aws_sdk_athena.types.s3_uri.S3Uri"]
    """<p>A URI that specifies the Amazon S3 location of a notebook file in <code>ipynb</code> format.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_athena.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to import the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportNotebookInput) -> dict:
    out: dict = {}
    out["WorkGroup"] = value["work_group"]
    out["Name"] = value["name"]
    if "payload" in value:
        out["Payload"] = value["payload"]
    import aws_sdk_athena.types.notebook_type

    out["Type"] = aws_sdk_athena.types.notebook_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "notebook_s3_location_uri" in value:
        out["NotebookS3LocationUri"] = value["notebook_s3_location_uri"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportNotebookInput:
    out: ImportNotebookInput = {}  # type: ignore[typeddict-item]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    else:
        raise DeserializationError("ImportNotebookInput.work_group required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ImportNotebookInput.name required")
    if "Payload" in data:
        out["payload"] = data["Payload"]
    if "Type" in data:
        import aws_sdk_athena.types.notebook_type

        out["type"] = aws_sdk_athena.types.notebook_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("ImportNotebookInput.type required")
    if "NotebookS3LocationUri" in data:
        out["notebook_s3_location_uri"] = data["NotebookS3LocationUri"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out

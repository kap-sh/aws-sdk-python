"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateRetrieverRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.retriever_configuration
    import aws_sdk_qbusiness.types.retriever_id
    import aws_sdk_qbusiness.types.retriever_name
    import aws_sdk_qbusiness.types.role_arn


class UpdateRetrieverRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of your Amazon Q Business application.</p>"""
    retriever_id: "aws_sdk_qbusiness.types.retriever_id.RetrieverId"
    """<p>The identifier of your retriever.</p>"""
    configuration: NotRequired[
        "aws_sdk_qbusiness.types.retriever_configuration.RetrieverConfiguration"
    ]
    display_name: NotRequired["aws_sdk_qbusiness.types.retriever_name.RetrieverName"]
    """<p>The name of your retriever.</p>"""
    role_arn: NotRequired["aws_sdk_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the retriever and required resources. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRetrieverRequest) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_qbusiness.types.retriever_configuration

        out["configuration"] = (
            aws_sdk_qbusiness.types.retriever_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateRetrieverRequest:
    out: UpdateRetrieverRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_qbusiness.types.retriever_configuration

        out["configuration"] = (
            aws_sdk_qbusiness.types.retriever_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetRetrieverResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.retriever_arn
    import aws_sdk_qbusiness.types.retriever_configuration
    import aws_sdk_qbusiness.types.retriever_id
    import aws_sdk_qbusiness.types.retriever_name
    import aws_sdk_qbusiness.types.retriever_status
    import aws_sdk_qbusiness.types.retriever_type
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.timestamp


class GetRetrieverResponse(TypedDict):
    application_id: NotRequired["aws_sdk_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application using the retriever. </p>"""
    retriever_id: NotRequired["aws_sdk_qbusiness.types.retriever_id.RetrieverId"]
    """<p>The identifier of the retriever.</p>"""
    retriever_arn: NotRequired["aws_sdk_qbusiness.types.retriever_arn.RetrieverArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the retriever.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.retriever_type.RetrieverType"]
    """<p>The type of the retriever.</p>"""
    status: NotRequired["aws_sdk_qbusiness.types.retriever_status.RetrieverStatus"]
    """<p>The status of the retriever.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.retriever_name.RetrieverName"]
    """<p>The name of the retriever.</p>"""
    configuration: NotRequired[
        "aws_sdk_qbusiness.types.retriever_configuration.RetrieverConfiguration"
    ]
    role_arn: NotRequired["aws_sdk_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role with the permission to access the retriever and required resources.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the retriever was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the retriever was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetrieverResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "retriever_id" in value:
        out["retrieverId"] = value["retriever_id"]
    if "retriever_arn" in value:
        out["retrieverArn"] = value["retriever_arn"]
    if "type" in value:
        import aws_sdk_qbusiness.types.retriever_type

        out["type"] = aws_sdk_qbusiness.types.retriever_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_qbusiness.types.retriever_status

        out["status"] = aws_sdk_qbusiness.types.retriever_status.serialize_json(
            value["status"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "configuration" in value:
        import aws_sdk_qbusiness.types.retriever_configuration

        out["configuration"] = (
            aws_sdk_qbusiness.types.retriever_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetRetrieverResponse:
    out: GetRetrieverResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "retrieverId" in data:
        out["retriever_id"] = data["retrieverId"]
    if "retrieverArn" in data:
        out["retriever_arn"] = data["retrieverArn"]
    if "type" in data:
        import aws_sdk_qbusiness.types.retriever_type

        out["type"] = aws_sdk_qbusiness.types.retriever_type.deserialize_json(
            data["type"]
        )
    if "status" in data:
        import aws_sdk_qbusiness.types.retriever_status

        out["status"] = aws_sdk_qbusiness.types.retriever_status.deserialize_json(
            data["status"]
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "configuration" in data:
        import aws_sdk_qbusiness.types.retriever_configuration

        out["configuration"] = (
            aws_sdk_qbusiness.types.retriever_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out

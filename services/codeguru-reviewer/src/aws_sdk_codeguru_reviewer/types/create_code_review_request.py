"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#CreateCodeReviewRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.association_arn
    import aws_sdk_codeguru_reviewer.types.client_request_token
    import aws_sdk_codeguru_reviewer.types.code_review_name
    import aws_sdk_codeguru_reviewer.types.code_review_type


class CreateCodeReviewRequest(TypedDict):
    name: "aws_sdk_codeguru_reviewer.types.code_review_name.CodeReviewName"
    """<p>The name of the code review. The name of each code review in your Amazon Web Services account must be unique.</p>"""
    repository_association_arn: (
        "aws_sdk_codeguru_reviewer.types.association_arn.AssociationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html\">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html\">ListRepositoryAssociations</a>.</p> <p>A code review can only be created on an associated repository. This is the ARN of the associated repository.</p>"""
    type: "aws_sdk_codeguru_reviewer.types.code_review_type.CodeReviewType"
    """<p>The type of code review to create. This is specified using a <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html\">CodeReviewType</a> object. You can create a code review only of type <code>RepositoryAnalysis</code>.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_codeguru_reviewer.types.client_request_token.ClientRequestToken"
    ]
    """<p>Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate code reviews if there are failures and retries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeReviewRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RepositoryAssociationArn"] = value["repository_association_arn"]
    import aws_sdk_codeguru_reviewer.types.code_review_type

    out["Type"] = aws_sdk_codeguru_reviewer.types.code_review_type.serialize_json(
        value["type"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateCodeReviewRequest:
    out: CreateCodeReviewRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCodeReviewRequest.name required")
    if "RepositoryAssociationArn" in data:
        out["repository_association_arn"] = data["RepositoryAssociationArn"]
    else:
        raise DeserializationError(
            "CreateCodeReviewRequest.repository_association_arn required"
        )
    if "Type" in data:
        import aws_sdk_codeguru_reviewer.types.code_review_type

        out["type"] = aws_sdk_codeguru_reviewer.types.code_review_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateCodeReviewRequest.type required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeDocumentPermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_name
    import aws_sdk_ssm.types.document_permission_max_results
    import aws_sdk_ssm.types.document_permission_type
    import aws_sdk_ssm.types.next_token


class DescribeDocumentPermissionRequest(TypedDict):
    name: "aws_sdk_ssm.types.document_name.DocumentName"
    """<p>The name of the document for which you are the owner. </p>"""
    permission_type: "aws_sdk_ssm.types.document_permission_type.DocumentPermissionType"
    """<p>The permission type for the document. The permission type can be <i>Share</i>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ssm.types.document_permission_max_results.DocumentPermissionMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentPermissionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_ssm.types.document_permission_type

    out["PermissionType"] = (
        aws_sdk_ssm.types.document_permission_type.serialize_aws_json_1_1(
            value["permission_type"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentPermissionRequest:
    out: DescribeDocumentPermissionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeDocumentPermissionRequest.name required")
    if "PermissionType" in data:
        import aws_sdk_ssm.types.document_permission_type

        out["permission_type"] = (
            aws_sdk_ssm.types.document_permission_type.deserialize_aws_json_1_1(
                data["PermissionType"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDocumentPermissionRequest.permission_type required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

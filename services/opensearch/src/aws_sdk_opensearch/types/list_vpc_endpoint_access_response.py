"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVpcEndpointAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.authorized_principal_list
    import aws_sdk_opensearch.types.next_token


class ListVpcEndpointAccessResponse(TypedDict, closed=True):
    authorized_principal_list: (
        "aws_sdk_opensearch.types.authorized_principal_list.AuthorizedPrincipalList"
    )
    r"""<p>A list of <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html\">IAM principals</a> that can currently access the domain.</p>"""
    next_token: "aws_sdk_opensearch.types.next_token.NextToken"
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointAccessResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.authorized_principal_list

    out["AuthorizedPrincipalList"] = (
        aws_sdk_opensearch.types.authorized_principal_list.serialize_json(
            value["authorized_principal_list"]
        )
    )
    out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcEndpointAccessResponse:
    out: ListVpcEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedPrincipalList" in data:
        import aws_sdk_opensearch.types.authorized_principal_list

        out["authorized_principal_list"] = (
            aws_sdk_opensearch.types.authorized_principal_list.deserialize_json(
                data["AuthorizedPrincipalList"]
            )
        )
    else:
        raise DeserializationError(
            "ListVpcEndpointAccessResponse.authorized_principal_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    else:
        raise DeserializationError("ListVpcEndpointAccessResponse.next_token required")
    return out

"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListNamespacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace_list


class ListNamespacesResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    namespaces: "aws_sdk_redshift_serverless.types.namespace_list.NamespaceList"
    """<p>The list of returned namespaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNamespacesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_redshift_serverless.types.namespace_list

    out["namespaces"] = (
        aws_sdk_redshift_serverless.types.namespace_list.serialize_aws_json_1_1(
            value["namespaces"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNamespacesResponse:
    out: ListNamespacesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "namespaces" in data:
        import aws_sdk_redshift_serverless.types.namespace_list

        out["namespaces"] = (
            aws_sdk_redshift_serverless.types.namespace_list.deserialize_aws_json_1_1(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("ListNamespacesResponse.namespaces required")
    return out

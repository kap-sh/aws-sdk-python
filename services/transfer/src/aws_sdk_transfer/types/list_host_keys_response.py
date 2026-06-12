"""Generated from Smithy shape ``com.amazonaws.transfer#ListHostKeysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_host_keys
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.server_id


class ListHostKeysResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListHostKeys</code> again and receive additional results, if there are any.</p>"""
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>Returns the server identifier that contains the listed host keys.</p>"""
    host_keys: "aws_sdk_transfer.types.listed_host_keys.ListedHostKeys"
    """<p>Returns an array, where each item contains the details of a host key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHostKeysResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    import aws_sdk_transfer.types.listed_host_keys

    out["HostKeys"] = aws_sdk_transfer.types.listed_host_keys.serialize_aws_json_1_1(
        value["host_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHostKeysResponse:
    out: ListHostKeysResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ListHostKeysResponse.server_id required")
    if "HostKeys" in data:
        import aws_sdk_transfer.types.listed_host_keys

        out["host_keys"] = (
            aws_sdk_transfer.types.listed_host_keys.deserialize_aws_json_1_1(
                data["HostKeys"]
            )
        )
    else:
        raise DeserializationError("ListHostKeysResponse.host_keys required")
    return out

"""Generated from Smithy shape ``com.amazonaws.transfer#ListAccessesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_accesses
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.server_id


class ListAccessesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListAccesses</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional accesses.</p>"""
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that has users assigned to it.</p>"""
    accesses: "aws_sdk_transfer.types.listed_accesses.ListedAccesses"
    """<p>Returns the accesses and their properties for the <code>ServerId</code> value that you specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccessesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    import aws_sdk_transfer.types.listed_accesses

    out["Accesses"] = aws_sdk_transfer.types.listed_accesses.serialize_aws_json_1_1(
        value["accesses"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccessesResponse:
    out: ListAccessesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("ListAccessesResponse.server_id required")
    if "Accesses" in data:
        import aws_sdk_transfer.types.listed_accesses

        out["accesses"] = (
            aws_sdk_transfer.types.listed_accesses.deserialize_aws_json_1_1(
                data["Accesses"]
            )
        )
    else:
        raise DeserializationError("ListAccessesResponse.accesses required")
    return out

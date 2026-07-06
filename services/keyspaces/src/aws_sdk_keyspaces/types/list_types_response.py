"""Generated from Smithy shape ``com.amazonaws.keyspaces#ListTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.next_token
    import aws_sdk_keyspaces.types.type_name_list


class ListTypesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_keyspaces.types.next_token.NextToken"]
    """<p> The pagination token. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation. </p>"""
    types: "aws_sdk_keyspaces.types.type_name_list.TypeNameList"
    """<p> The list of types contained in the specified keyspace. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTypesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_keyspaces.types.type_name_list

    out["types"] = aws_sdk_keyspaces.types.type_name_list.serialize_aws_json_1_0(
        value["types"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTypesResponse:
    out: ListTypesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "types" in data:
        import aws_sdk_keyspaces.types.type_name_list

        out["types"] = aws_sdk_keyspaces.types.type_name_list.deserialize_aws_json_1_0(
            data["types"]
        )
    else:
        raise DeserializationError("ListTypesResponse.types required")
    return out

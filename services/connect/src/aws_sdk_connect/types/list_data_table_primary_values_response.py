"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTablePrimaryValuesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.primary_values_list


class ListDataTablePrimaryValuesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    primary_values_list: "aws_sdk_connect.types.primary_values_list.PrimaryValuesList"
    """<p>A list of primary value combinations with their record IDs and modification metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTablePrimaryValuesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_connect.types.primary_values_list

    out["PrimaryValuesList"] = aws_sdk_connect.types.primary_values_list.serialize_json(
        value["primary_values_list"]
    )
    return out


def deserialize_json(data: dict) -> ListDataTablePrimaryValuesResponse:
    out: ListDataTablePrimaryValuesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PrimaryValuesList" in data:
        import aws_sdk_connect.types.primary_values_list

        out["primary_values_list"] = (
            aws_sdk_connect.types.primary_values_list.deserialize_json(
                data["PrimaryValuesList"]
            )
        )
    else:
        raise DeserializationError(
            "ListDataTablePrimaryValuesResponse.primary_values_list required"
        )
    return out

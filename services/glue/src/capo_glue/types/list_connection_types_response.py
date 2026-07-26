"""Generated from Smithy shape ``com.amazonaws.glue#ListConnectionTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_type_list
    import capo_glue.types.next_token


class ListConnectionTypesResponse(TypedDict, closed=True):
    connection_types: NotRequired[
        "capo_glue.types.connection_type_list.ConnectionTypeList"
    ]
    """<p>A list of <code>ConnectionTypeBrief</code> objects containing brief information about the supported connection types.</p>"""
    next_token: NotRequired["capo_glue.types.next_token.NextToken"]
    """<p>A continuation token, if the current list segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConnectionTypesResponse) -> dict:
    out: dict = {}
    if "connection_types" in value:
        import capo_glue.types.connection_type_list

        out["ConnectionTypes"] = (
            capo_glue.types.connection_type_list.serialize_aws_json_1_1(
                value["connection_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConnectionTypesResponse:
    out: ListConnectionTypesResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionTypes" in data:
        import capo_glue.types.connection_type_list

        out["connection_types"] = (
            capo_glue.types.connection_type_list.deserialize_aws_json_1_1(
                data["ConnectionTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

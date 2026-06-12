"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListTestSetRecordsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.test_set_turn_record_list


class ListTestSetRecordsResponse(TypedDict):
    test_set_records: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_turn_record_list.TestSetTurnRecordList"
    ]
    """<p>The list of records from the test set.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more records to return in a response to the ListTestSetRecords operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListTestSetRecords operation request to get the next page of records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestSetRecordsResponse) -> dict:
    out: dict = {}
    if "test_set_records" in value:
        import aws_sdk_lex_models_v2.types.test_set_turn_record_list

        out["testSetRecords"] = (
            aws_sdk_lex_models_v2.types.test_set_turn_record_list.serialize_json(
                value["test_set_records"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestSetRecordsResponse:
    out: ListTestSetRecordsResponse = {}  # type: ignore[typeddict-item]
    if "testSetRecords" in data:
        import aws_sdk_lex_models_v2.types.test_set_turn_record_list

        out["test_set_records"] = (
            aws_sdk_lex_models_v2.types.test_set_turn_record_list.deserialize_json(
                data["testSetRecords"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

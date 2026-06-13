"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListJournalRecordsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.journal_record_list


class ListJournalRecordsResponse(TypedDict):
    records: "aws_sdk_devops_agent.types.journal_record_list.JournalRecordList"
    """<p>List of journal records matching the request criteria</p>"""
    next_token: NotRequired["str"]
    """<p>Token for retrieving the next page of results, if more results are available</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJournalRecordsResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.journal_record_list

    out["records"] = aws_sdk_devops_agent.types.journal_record_list.serialize_json(
        value["records"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJournalRecordsResponse:
    out: ListJournalRecordsResponse = {}  # type: ignore[typeddict-item]
    if "records" in data:
        import aws_sdk_devops_agent.types.journal_record_list

        out["records"] = (
            aws_sdk_devops_agent.types.journal_record_list.deserialize_json(
                data["records"]
            )
        )
    else:
        raise DeserializationError("ListJournalRecordsResponse.records required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

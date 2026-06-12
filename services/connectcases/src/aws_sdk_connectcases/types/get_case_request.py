"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.field_identifier_list
    import aws_sdk_connectcases.types.next_token


class GetCaseRequest(TypedDict):
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    fields: "aws_sdk_connectcases.types.field_identifier_list.FieldIdentifierList"
    """<p>A list of unique field identifiers. </p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.field_identifier_list

    out["fields"] = aws_sdk_connectcases.types.field_identifier_list.serialize_json(
        value["fields"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCaseRequest:
    out: GetCaseRequest = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.field_identifier_list

        out["fields"] = (
            aws_sdk_connectcases.types.field_identifier_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("GetCaseRequest.fields required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

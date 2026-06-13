"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_value_list
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.tags
    import aws_sdk_connectcases.types.template_id


class GetCaseResponse(TypedDict):
    fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList"
    """<p>A list of detailed field information. </p>"""
    template_id: "aws_sdk_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseResponse) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.field_value_list

    out["fields"] = aws_sdk_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    out["templateId"] = value["template_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCaseResponse:
    out: GetCaseResponse = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.field_value_list

        out["fields"] = aws_sdk_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("GetCaseResponse.fields required")
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("GetCaseResponse.template_id required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    return out

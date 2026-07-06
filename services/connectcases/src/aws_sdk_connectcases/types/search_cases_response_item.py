"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchCasesResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.field_value_list
    import aws_sdk_connectcases.types.tags
    import aws_sdk_connectcases.types.template_id


class SearchCasesResponseItem(TypedDict, closed=True):
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    template_id: "aws_sdk_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList"
    """<p>List of case field values.</p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchCasesResponseItem) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    out["templateId"] = value["template_id"]
    import aws_sdk_connectcases.types.field_value_list

    out["fields"] = aws_sdk_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SearchCasesResponseItem:
    out: SearchCasesResponseItem = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("SearchCasesResponseItem.case_id required")
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("SearchCasesResponseItem.template_id required")
    if "fields" in data:
        import aws_sdk_connectcases.types.field_value_list

        out["fields"] = aws_sdk_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("SearchCasesResponseItem.fields required")
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    return out

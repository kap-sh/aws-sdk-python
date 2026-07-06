"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.field_value_list
    import aws_sdk_connectcases.types.mutable_tags
    import aws_sdk_connectcases.types.template_id
    import aws_sdk_connectcases.types.user_union


class CreateCaseRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    template_id: "aws_sdk_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    fields: "aws_sdk_connectcases.types.field_value_list.FieldValueList"
    """<p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>"""
    client_token: NotRequired["str"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    performed_by: NotRequired["aws_sdk_connectcases.types.user_union.UserUnion"]
    tags: NotRequired["aws_sdk_connectcases.types.mutable_tags.MutableTags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseRequest) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    import aws_sdk_connectcases.types.field_value_list

    out["fields"] = aws_sdk_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "performed_by" in value:
        import aws_sdk_connectcases.types.user_union

        out["performedBy"] = aws_sdk_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    if "tags" in value:
        import aws_sdk_connectcases.types.mutable_tags

        out["tags"] = aws_sdk_connectcases.types.mutable_tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCaseRequest:
    out: CreateCaseRequest = {}  # type: ignore[typeddict-item]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("CreateCaseRequest.template_id required")
    if "fields" in data:
        import aws_sdk_connectcases.types.field_value_list

        out["fields"] = aws_sdk_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("CreateCaseRequest.fields required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "performedBy" in data:
        import aws_sdk_connectcases.types.user_union

        out["performed_by"] = aws_sdk_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    if "tags" in data:
        import aws_sdk_connectcases.types.mutable_tags

        out["tags"] = aws_sdk_connectcases.types.mutable_tags.deserialize_json(
            data["tags"]
        )
    return out

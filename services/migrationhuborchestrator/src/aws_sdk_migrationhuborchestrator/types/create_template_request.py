"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.client_token
    import aws_sdk_migrationhuborchestrator.types.tag_map
    import aws_sdk_migrationhuborchestrator.types.template_source


class CreateTemplateRequest(TypedDict):
    template_name: "str"
    """<p>The name of the migration workflow template.</p>"""
    template_description: NotRequired["str"]
    """<p>A description of the migration workflow template.</p>"""
    template_source: (
        "aws_sdk_migrationhuborchestrator.types.template_source.TemplateSource"
    )
    """<p>The source of the migration workflow template.</p>"""
    client_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.client_token.ClientToken"
    ]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://smithy.io/2.0/spec/behavior-traits.html#idempotencytoken-trait\">Idempotency</a> in the Smithy documentation.</p>"""
    tags: NotRequired["aws_sdk_migrationhuborchestrator.types.tag_map.TagMap"]
    """<p>The tags to add to the migration workflow template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateRequest) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    if "template_description" in value:
        out["templateDescription"] = value["template_description"]
    import aws_sdk_migrationhuborchestrator.types.template_source

    out["templateSource"] = (
        aws_sdk_migrationhuborchestrator.types.template_source.serialize_json(
            value["template_source"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_migrationhuborchestrator.types.tag_map

        out["tags"] = aws_sdk_migrationhuborchestrator.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("CreateTemplateRequest.template_name required")
    if "templateDescription" in data:
        out["template_description"] = data["templateDescription"]
    if "templateSource" in data:
        import aws_sdk_migrationhuborchestrator.types.template_source

        out["template_source"] = (
            aws_sdk_migrationhuborchestrator.types.template_source.deserialize_json(
                data["templateSource"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateRequest.template_source required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_migrationhuborchestrator.types.tag_map

        out["tags"] = aws_sdk_migrationhuborchestrator.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out

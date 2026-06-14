"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGlossaryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.glossary_description
    import aws_sdk_datazone.types.glossary_id
    import aws_sdk_datazone.types.glossary_name
    import aws_sdk_datazone.types.glossary_status


class UpdateGlossaryInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the business glossary to be updated.</p>"""
    name: NotRequired["aws_sdk_datazone.types.glossary_name.GlossaryName"]
    """<p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    status: NotRequired["aws_sdk_datazone.types.glossary_status.GlossaryStatus"]
    """<p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlossaryInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_datazone.types.glossary_status

        out["status"] = aws_sdk_datazone.types.glossary_status.serialize_json(
            value["status"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateGlossaryInput:
    out: UpdateGlossaryInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.glossary_status

        out["status"] = aws_sdk_datazone.types.glossary_status.deserialize_json(
            data["status"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

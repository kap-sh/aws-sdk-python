"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGlossaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_description
    import capo_datazone.types.glossary_id
    import capo_datazone.types.glossary_name
    import capo_datazone.types.glossary_status


class UpdateGlossaryInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>"""
    identifier: "capo_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the business glossary to be updated.</p>"""
    name: NotRequired["capo_datazone.types.glossary_name.GlossaryName"]
    """<p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    description: NotRequired[
        "capo_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    status: NotRequired["capo_datazone.types.glossary_status.GlossaryStatus"]
    """<p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlossaryInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_datazone.types.glossary_status

        out["status"] = capo_datazone.types.glossary_status.serialize_json(
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
        import capo_datazone.types.glossary_status

        out["status"] = capo_datazone.types.glossary_status.deserialize_json(
            data["status"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

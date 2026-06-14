"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDataProductInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.data_product_description
    import aws_sdk_datazone.types.data_product_items
    import aws_sdk_datazone.types.data_product_name
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_input_list
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_id


class CreateDataProductInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data product is created.</p>"""
    name: "aws_sdk_datazone.types.data_product_name.DataProductName"
    """<p>The name of the data product.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the owning project of the data product.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.data_product_description.DataProductDescription"
    ]
    """<p>The description of the data product.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms of the data product.</p>"""
    forms_input: NotRequired["aws_sdk_datazone.types.form_input_list.FormInputList"]
    """<p>The metadata forms of the data product.</p>"""
    items: NotRequired["aws_sdk_datazone.types.data_product_items.DataProductItems"]
    """<p>The data assets of the data product.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataProductInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "forms_input" in value:
        import aws_sdk_datazone.types.form_input_list

        out["formsInput"] = aws_sdk_datazone.types.form_input_list.serialize_json(
            value["forms_input"]
        )
    if "items" in value:
        import aws_sdk_datazone.types.data_product_items

        out["items"] = aws_sdk_datazone.types.data_product_items.serialize_json(
            value["items"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDataProductInput:
    out: CreateDataProductInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDataProductInput.name required")
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateDataProductInput.owning_project_identifier required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "formsInput" in data:
        import aws_sdk_datazone.types.form_input_list

        out["forms_input"] = aws_sdk_datazone.types.form_input_list.deserialize_json(
            data["formsInput"]
        )
    if "items" in data:
        import aws_sdk_datazone.types.data_product_items

        out["items"] = aws_sdk_datazone.types.data_product_items.deserialize_json(
            data["items"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

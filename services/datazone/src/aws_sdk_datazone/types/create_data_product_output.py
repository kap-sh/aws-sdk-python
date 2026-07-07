"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDataProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.data_product_description
    import aws_sdk_datazone.types.data_product_id
    import aws_sdk_datazone.types.data_product_items
    import aws_sdk_datazone.types.data_product_name
    import aws_sdk_datazone.types.data_product_status
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_output_list
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision


class CreateDataProductOutput(TypedDict, closed=True):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data product lives.</p>"""
    id: "aws_sdk_datazone.types.data_product_id.DataProductId"
    """<p>The ID of the data product.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of the data product.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the owning project of the data product.</p>"""
    name: "aws_sdk_datazone.types.data_product_name.DataProductName"
    """<p>The name of the data product.</p>"""
    status: "aws_sdk_datazone.types.data_product_status.DataProductStatus"
    """<p>The status of the data product.</p>"""
    description: NotRequired[
        "aws_sdk_datazone.types.data_product_description.DataProductDescription"
    ]
    """<p>The description of the data product.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms of the data product.</p>"""
    items: NotRequired["aws_sdk_datazone.types.data_product_items.DataProductItems"]
    """<p>The data assets of the data product.</p>"""
    forms_output: NotRequired["aws_sdk_datazone.types.form_output_list.FormOutputList"]
    """<p>The metadata forms of the data product.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data product was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data product.</p>"""
    first_revision_created_at: NotRequired[
        "aws_sdk_datazone.types.created_at.CreatedAt"
    ]
    """<p>The timestamp at which the first revision of the data product was created.</p>"""
    first_revision_created_by: NotRequired[
        "aws_sdk_datazone.types.created_by.CreatedBy"
    ]
    """<p>The user who created the first revision of the data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataProductOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["revision"] = value["revision"]
    out["owningProjectId"] = value["owning_project_id"]
    out["name"] = value["name"]
    import aws_sdk_datazone.types.data_product_status

    out["status"] = aws_sdk_datazone.types.data_product_status.serialize_json(
        value.get("status", "CREATED")
    )
    if "description" in value:
        out["description"] = value["description"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "items" in value:
        import aws_sdk_datazone.types.data_product_items

        out["items"] = aws_sdk_datazone.types.data_product_items.serialize_json(
            value["items"]
        )
    if "forms_output" in value:
        import aws_sdk_datazone.types.form_output_list

        out["formsOutput"] = aws_sdk_datazone.types.form_output_list.serialize_json(
            value["forms_output"]
        )
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "first_revision_created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["firstRevisionCreatedAt"] = (
            aws_sdk_datazone.types.created_at.serialize_json(
                value["first_revision_created_at"]
            )
        )
    if "first_revision_created_by" in value:
        out["firstRevisionCreatedBy"] = value["first_revision_created_by"]
    return out


def deserialize_json(data: dict) -> CreateDataProductOutput:
    out: CreateDataProductOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateDataProductOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateDataProductOutput.id required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("CreateDataProductOutput.revision required")
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("CreateDataProductOutput.owning_project_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDataProductOutput.name required")
    if "status" in data:
        import aws_sdk_datazone.types.data_product_status

        out["status"] = aws_sdk_datazone.types.data_product_status.deserialize_json(
            data["status"]
        )
    else:
        out["status"] = "CREATED"
    if "description" in data:
        out["description"] = data["description"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "items" in data:
        import aws_sdk_datazone.types.data_product_items

        out["items"] = aws_sdk_datazone.types.data_product_items.deserialize_json(
            data["items"]
        )
    if "formsOutput" in data:
        import aws_sdk_datazone.types.form_output_list

        out["forms_output"] = aws_sdk_datazone.types.form_output_list.deserialize_json(
            data["formsOutput"]
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "firstRevisionCreatedAt" in data:
        import aws_sdk_datazone.types.created_at

        out["first_revision_created_at"] = (
            aws_sdk_datazone.types.created_at.deserialize_json(
                data["firstRevisionCreatedAt"]
            )
        )
    if "firstRevisionCreatedBy" in data:
        out["first_revision_created_by"] = data["firstRevisionCreatedBy"]
    return out

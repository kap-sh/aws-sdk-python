"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_name
    import aws_sdk_datazone.types.asset_type_identifier
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.external_identifier
    import aws_sdk_datazone.types.form_input_list
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.prediction_configuration
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision


class CreateAssetInput(TypedDict):
    name: "aws_sdk_datazone.types.asset_name.AssetName"
    """<p>Asset name.</p>"""
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>Amazon DataZone domain where the asset is created.</p>"""
    external_identifier: NotRequired[
        "aws_sdk_datazone.types.external_identifier.ExternalIdentifier"
    ]
    """<p>The external identifier of the asset.</p> <p>If the value for the <code>externalIdentifier</code> parameter is specified, it must be a unique value.</p>"""
    type_identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier"
    """<p>The unique identifier of this asset's type.</p>"""
    type_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of this asset's type.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>Asset description.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>Glossary terms attached to the asset.</p>"""
    forms_input: NotRequired["aws_sdk_datazone.types.form_input_list.FormInputList"]
    """<p>Metadata forms attached to the asset.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The unique identifier of the project that owns this asset.</p>"""
    prediction_configuration: NotRequired[
        "aws_sdk_datazone.types.prediction_configuration.PredictionConfiguration"
    ]
    """<p>The configuration of the automatically generated business-friendly metadata for the asset.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "external_identifier" in value:
        out["externalIdentifier"] = value["external_identifier"]
    out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
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
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    if "prediction_configuration" in value:
        import aws_sdk_datazone.types.prediction_configuration

        out["predictionConfiguration"] = (
            aws_sdk_datazone.types.prediction_configuration.serialize_json(
                value["prediction_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssetInput:
    out: CreateAssetInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetInput.name required")
    if "externalIdentifier" in data:
        out["external_identifier"] = data["externalIdentifier"]
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError("CreateAssetInput.type_identifier required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
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
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateAssetInput.owning_project_identifier required"
        )
    if "predictionConfiguration" in data:
        import aws_sdk_datazone.types.prediction_configuration

        out["prediction_configuration"] = (
            aws_sdk_datazone.types.prediction_configuration.deserialize_json(
                data["predictionConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

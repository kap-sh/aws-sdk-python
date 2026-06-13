"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetRevisionInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.asset_name
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_input_list
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.prediction_configuration
    import aws_sdk_datazone.types.revision


class CreateAssetRevisionInput(TypedDict):
    name: "aws_sdk_datazone.types.asset_name.AssetName"
    """<p>Te revised name of the asset.</p>"""
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The unique identifier of the domain where the asset is being revised.</p>"""
    identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the asset.</p>"""
    type_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision type of the asset.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The revised description of the asset.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be attached to the asset as part of asset revision.</p>"""
    forms_input: NotRequired["aws_sdk_datazone.types.form_input_list.FormInputList"]
    """<p>The metadata forms to be attached to the asset as part of asset revision.</p>"""
    prediction_configuration: NotRequired[
        "aws_sdk_datazone.types.prediction_configuration.PredictionConfiguration"
    ]
    """<p>The configuration of the automatically generated business-friendly metadata for the asset.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetRevisionInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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


def deserialize_json(data: dict) -> CreateAssetRevisionInput:
    out: CreateAssetRevisionInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetRevisionInput.name required")
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

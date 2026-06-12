"""Generated from Smithy shape ``com.amazonaws.b2bi#GetTransformerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.created_date
    import aws_sdk_b2bi.types.edi_type
    import aws_sdk_b2bi.types.file_format
    import aws_sdk_b2bi.types.file_location
    import aws_sdk_b2bi.types.input_conversion
    import aws_sdk_b2bi.types.mapping
    import aws_sdk_b2bi.types.mapping_template
    import aws_sdk_b2bi.types.modified_date
    import aws_sdk_b2bi.types.output_conversion
    import aws_sdk_b2bi.types.resource_arn
    import aws_sdk_b2bi.types.sample_documents
    import aws_sdk_b2bi.types.transformer_id
    import aws_sdk_b2bi.types.transformer_name
    import aws_sdk_b2bi.types.transformer_status


class GetTransformerResponse(TypedDict):
    transformer_id: "aws_sdk_b2bi.types.transformer_id.TransformerId"
    """<p>Returns the system-assigned unique identifier for the transformer.</p>"""
    transformer_arn: "aws_sdk_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    name: "aws_sdk_b2bi.types.transformer_name.TransformerName"
    """<p>Returns the name of the transformer, used to identify it.</p>"""
    status: "aws_sdk_b2bi.types.transformer_status.TransformerStatus"
    """<p>Returns the state of the newly created transformer. The transformer can be either <code>active</code> or <code>inactive</code>. For the transformer to be used in a capability, its status must <code>active</code>.</p>"""
    created_at: "aws_sdk_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the transformer.</p>"""
    modified_at: NotRequired["aws_sdk_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp for last time the transformer was modified.</p>"""
    file_format: "aws_sdk_b2bi.types.file_format.FileFormat"
    """<p>Returns that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>"""
    mapping_template: "aws_sdk_b2bi.types.mapping_template.MappingTemplate"
    """<p>Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p>"""
    edi_type: NotRequired["aws_sdk_b2bi.types.edi_type.EdiType"]
    """<p>Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>"""
    sample_document: NotRequired["aws_sdk_b2bi.types.file_location.FileLocation"]
    """<p>Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>"""
    input_conversion: NotRequired["aws_sdk_b2bi.types.input_conversion.InputConversion"]
    """<p>Returns the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>"""
    mapping: NotRequired["aws_sdk_b2bi.types.mapping.Mapping"]
    """<p>Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>"""
    output_conversion: NotRequired[
        "aws_sdk_b2bi.types.output_conversion.OutputConversion"
    ]
    """<p>Returns the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>"""
    sample_documents: NotRequired["aws_sdk_b2bi.types.sample_documents.SampleDocuments"]
    """<p>Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTransformerResponse) -> dict:
    out: dict = {}
    out["transformerId"] = value["transformer_id"]
    out["transformerArn"] = value["transformer_arn"]
    out["name"] = value["name"]
    import aws_sdk_b2bi.types.transformer_status

    out["status"] = aws_sdk_b2bi.types.transformer_status.serialize_aws_json_1_0(
        value["status"]
    )
    import aws_sdk_b2bi.types.created_date

    out["createdAt"] = aws_sdk_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import aws_sdk_b2bi.types.modified_date

        out["modifiedAt"] = aws_sdk_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    import aws_sdk_b2bi.types.file_format

    out["fileFormat"] = aws_sdk_b2bi.types.file_format.serialize_aws_json_1_0(
        value.get("file_format", "NOT_USED")
    )
    out["mappingTemplate"] = value.get("mapping_template", "NOT_USED")
    if "edi_type" in value:
        import aws_sdk_b2bi.types.edi_type

        out["ediType"] = aws_sdk_b2bi.types.edi_type.serialize_aws_json_1_0(
            value["edi_type"]
        )
    if "sample_document" in value:
        out["sampleDocument"] = value["sample_document"]
    if "input_conversion" in value:
        import aws_sdk_b2bi.types.input_conversion

        out["inputConversion"] = (
            aws_sdk_b2bi.types.input_conversion.serialize_aws_json_1_0(
                value["input_conversion"]
            )
        )
    if "mapping" in value:
        import aws_sdk_b2bi.types.mapping

        out["mapping"] = aws_sdk_b2bi.types.mapping.serialize_aws_json_1_0(
            value["mapping"]
        )
    if "output_conversion" in value:
        import aws_sdk_b2bi.types.output_conversion

        out["outputConversion"] = (
            aws_sdk_b2bi.types.output_conversion.serialize_aws_json_1_0(
                value["output_conversion"]
            )
        )
    if "sample_documents" in value:
        import aws_sdk_b2bi.types.sample_documents

        out["sampleDocuments"] = (
            aws_sdk_b2bi.types.sample_documents.serialize_aws_json_1_0(
                value["sample_documents"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTransformerResponse:
    out: GetTransformerResponse = {}  # type: ignore[typeddict-item]
    if "transformerId" in data:
        out["transformer_id"] = data["transformerId"]
    else:
        raise DeserializationError("GetTransformerResponse.transformer_id required")
    if "transformerArn" in data:
        out["transformer_arn"] = data["transformerArn"]
    else:
        raise DeserializationError("GetTransformerResponse.transformer_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetTransformerResponse.name required")
    if "status" in data:
        import aws_sdk_b2bi.types.transformer_status

        out["status"] = aws_sdk_b2bi.types.transformer_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("GetTransformerResponse.status required")
    if "createdAt" in data:
        import aws_sdk_b2bi.types.created_date

        out["created_at"] = aws_sdk_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetTransformerResponse.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_b2bi.types.modified_date

        out["modified_at"] = aws_sdk_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    if "fileFormat" in data:
        import aws_sdk_b2bi.types.file_format

        out["file_format"] = aws_sdk_b2bi.types.file_format.deserialize_aws_json_1_0(
            data["fileFormat"]
        )
    else:
        out["file_format"] = "NOT_USED"
    if "mappingTemplate" in data:
        out["mapping_template"] = data["mappingTemplate"]
    else:
        out["mapping_template"] = "NOT_USED"
    if "ediType" in data:
        import aws_sdk_b2bi.types.edi_type

        out["edi_type"] = aws_sdk_b2bi.types.edi_type.deserialize_aws_json_1_0(
            data["ediType"]
        )
    if "sampleDocument" in data:
        out["sample_document"] = data["sampleDocument"]
    if "inputConversion" in data:
        import aws_sdk_b2bi.types.input_conversion

        out["input_conversion"] = (
            aws_sdk_b2bi.types.input_conversion.deserialize_aws_json_1_0(
                data["inputConversion"]
            )
        )
    if "mapping" in data:
        import aws_sdk_b2bi.types.mapping

        out["mapping"] = aws_sdk_b2bi.types.mapping.deserialize_aws_json_1_0(
            data["mapping"]
        )
    if "outputConversion" in data:
        import aws_sdk_b2bi.types.output_conversion

        out["output_conversion"] = (
            aws_sdk_b2bi.types.output_conversion.deserialize_aws_json_1_0(
                data["outputConversion"]
            )
        )
    if "sampleDocuments" in data:
        import aws_sdk_b2bi.types.sample_documents

        out["sample_documents"] = (
            aws_sdk_b2bi.types.sample_documents.deserialize_aws_json_1_0(
                data["sampleDocuments"]
            )
        )
    return out

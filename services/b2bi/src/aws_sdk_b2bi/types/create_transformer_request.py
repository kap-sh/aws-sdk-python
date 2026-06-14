"""Generated from Smithy shape ``com.amazonaws.b2bi#CreateTransformerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.edi_type
    import aws_sdk_b2bi.types.file_format
    import aws_sdk_b2bi.types.file_location
    import aws_sdk_b2bi.types.input_conversion
    import aws_sdk_b2bi.types.mapping
    import aws_sdk_b2bi.types.mapping_template
    import aws_sdk_b2bi.types.output_conversion
    import aws_sdk_b2bi.types.sample_documents
    import aws_sdk_b2bi.types.tag_list
    import aws_sdk_b2bi.types.transformer_name


class CreateTransformerRequest(TypedDict):
    name: "aws_sdk_b2bi.types.transformer_name.TransformerName"
    """<p>Specifies the name of the transformer, used to identify it.</p>"""
    client_token: NotRequired["str"]
    """<p>Reserved for future use.</p>"""
    tags: NotRequired["aws_sdk_b2bi.types.tag_list.TagList"]
    """<p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>"""
    file_format: NotRequired["aws_sdk_b2bi.types.file_format.FileFormat"]
    """<p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>"""
    mapping_template: NotRequired["aws_sdk_b2bi.types.mapping_template.MappingTemplate"]
    r"""<p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href=\"https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html\">Mapping</a> data type instead.</p> </note>"""
    edi_type: NotRequired["aws_sdk_b2bi.types.edi_type.EdiType"]
    """<p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>"""
    sample_document: NotRequired["aws_sdk_b2bi.types.file_location.FileLocation"]
    """<p>Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>"""
    input_conversion: NotRequired["aws_sdk_b2bi.types.input_conversion.InputConversion"]
    """<p>Specify the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>"""
    mapping: NotRequired["aws_sdk_b2bi.types.mapping.Mapping"]
    """<p>Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>"""
    output_conversion: NotRequired[
        "aws_sdk_b2bi.types.output_conversion.OutputConversion"
    ]
    """<p>A structure that contains the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>"""
    sample_documents: NotRequired["aws_sdk_b2bi.types.sample_documents.SampleDocuments"]
    """<p>Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTransformerRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_b2bi.types.tag_list

        out["tags"] = aws_sdk_b2bi.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "file_format" in value:
        import aws_sdk_b2bi.types.file_format

        out["fileFormat"] = aws_sdk_b2bi.types.file_format.serialize_aws_json_1_0(
            value["file_format"]
        )
    if "mapping_template" in value:
        out["mappingTemplate"] = value["mapping_template"]
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


def deserialize_aws_json_1_0(data: dict) -> CreateTransformerRequest:
    out: CreateTransformerRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTransformerRequest.name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_b2bi.types.tag_list

        out["tags"] = aws_sdk_b2bi.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    if "fileFormat" in data:
        import aws_sdk_b2bi.types.file_format

        out["file_format"] = aws_sdk_b2bi.types.file_format.deserialize_aws_json_1_0(
            data["fileFormat"]
        )
    if "mappingTemplate" in data:
        out["mapping_template"] = data["mappingTemplate"]
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

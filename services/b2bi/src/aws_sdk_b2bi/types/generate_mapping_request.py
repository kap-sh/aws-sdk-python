"""Generated from Smithy shape ``com.amazonaws.b2bi#GenerateMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.generate_mapping_input_file_content
    import aws_sdk_b2bi.types.generate_mapping_output_file_content
    import aws_sdk_b2bi.types.mapping_type


class GenerateMappingRequest(TypedDict):
    input_file_content: "aws_sdk_b2bi.types.generate_mapping_input_file_content.GenerateMappingInputFileContent"
    """<p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a starting point for the mapping.</p>"""
    output_file_content: "aws_sdk_b2bi.types.generate_mapping_output_file_content.GenerateMappingOutputFileContent"
    """<p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a target for the mapping.</p>"""
    mapping_type: "aws_sdk_b2bi.types.mapping_type.MappingType"
    """<p>Specify the mapping type: either <code>JSONATA</code> or <code>XSLT.</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GenerateMappingRequest) -> dict:
    out: dict = {}
    out["inputFileContent"] = value["input_file_content"]
    out["outputFileContent"] = value["output_file_content"]
    import aws_sdk_b2bi.types.mapping_type

    out["mappingType"] = aws_sdk_b2bi.types.mapping_type.serialize_aws_json_1_0(
        value["mapping_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GenerateMappingRequest:
    out: GenerateMappingRequest = {}  # type: ignore[typeddict-item]
    if "inputFileContent" in data:
        out["input_file_content"] = data["inputFileContent"]
    else:
        raise DeserializationError("GenerateMappingRequest.input_file_content required")
    if "outputFileContent" in data:
        out["output_file_content"] = data["outputFileContent"]
    else:
        raise DeserializationError(
            "GenerateMappingRequest.output_file_content required"
        )
    if "mappingType" in data:
        import aws_sdk_b2bi.types.mapping_type

        out["mapping_type"] = aws_sdk_b2bi.types.mapping_type.deserialize_aws_json_1_0(
            data["mappingType"]
        )
    else:
        raise DeserializationError("GenerateMappingRequest.mapping_type required")
    return out

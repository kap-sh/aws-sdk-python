"""Generated from Smithy shape ``com.amazonaws.s3#SelectParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.expression
    import aws_sdk_s3.types.expression_type
    import aws_sdk_s3.types.input_serialization
    import aws_sdk_s3.types.output_serialization


class SelectParameters(TypedDict):
    input_serialization: "aws_sdk_s3.types.input_serialization.InputSerialization"
    """<p>Describes the serialization format of the object.</p>"""
    expression_type: "aws_sdk_s3.types.expression_type.ExpressionType"
    """<p>The type of the provided expression (for example, SQL).</p>"""
    expression: "aws_sdk_s3.types.expression.Expression"
    r"""<important> <p>Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. <a href=\"http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/\">Learn more</a> </p> </important> <p>The expression that is used to query the object.</p>"""
    output_serialization: "aws_sdk_s3.types.output_serialization.OutputSerialization"
    """<p>Describes how the results of the Select job are serialized.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SelectParameters, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.input_serialization

    aws_sdk_s3.types.input_serialization.serialize_xml(
        value["input_serialization"], el, "InputSerialization"
    )
    import aws_sdk_s3.types.expression_type

    aws_sdk_s3.types.expression_type.serialize_xml(
        value["expression_type"], el, "ExpressionType"
    )
    SubElement(el, "Expression").text = str(value["expression"])
    import aws_sdk_s3.types.output_serialization

    aws_sdk_s3.types.output_serialization.serialize_xml(
        value["output_serialization"], el, "OutputSerialization"
    )


def deserialize_xml(el: Element) -> SelectParameters:
    out: SelectParameters = {}  # type: ignore[typeddict-item]
    child_input_serialization = el.find("InputSerialization")
    if child_input_serialization is not None:
        import aws_sdk_s3.types.input_serialization

        out["input_serialization"] = (
            aws_sdk_s3.types.input_serialization.deserialize_xml(
                child_input_serialization
            )
        )
    else:
        raise DeserializationError("SelectParameters.input_serialization required")
    child_expression_type = el.find("ExpressionType")
    if child_expression_type is not None:
        import aws_sdk_s3.types.expression_type

        out["expression_type"] = aws_sdk_s3.types.expression_type.deserialize_xml(
            child_expression_type
        )
    else:
        raise DeserializationError("SelectParameters.expression_type required")
    child_expression = el.find("Expression")
    if child_expression is not None:
        out["expression"] = str(child_expression.text or "")
    else:
        raise DeserializationError("SelectParameters.expression required")
    child_output_serialization = el.find("OutputSerialization")
    if child_output_serialization is not None:
        import aws_sdk_s3.types.output_serialization

        out["output_serialization"] = (
            aws_sdk_s3.types.output_serialization.deserialize_xml(
                child_output_serialization
            )
        )
    else:
        raise DeserializationError("SelectParameters.output_serialization required")
    return out

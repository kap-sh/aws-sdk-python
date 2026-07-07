"""Generated from Smithy shape ``com.amazonaws.inspector#Exclusion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.attribute_list
    import aws_sdk_inspector.types.scope_list
    import aws_sdk_inspector.types.text


class Exclusion(TypedDict, closed=True):
    arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN that specifies the exclusion.</p>"""
    title: "aws_sdk_inspector.types.text.Text"
    """<p>The name of the exclusion.</p>"""
    description: "aws_sdk_inspector.types.text.Text"
    """<p>The description of the exclusion.</p>"""
    recommendation: "aws_sdk_inspector.types.text.Text"
    """<p>The recommendation for the exclusion.</p>"""
    scopes: "aws_sdk_inspector.types.scope_list.ScopeList"
    """<p>The AWS resources for which the exclusion pertains.</p>"""
    attributes: NotRequired["aws_sdk_inspector.types.attribute_list.AttributeList"]
    """<p>The system-defined attributes for the exclusion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Exclusion) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["title"] = value["title"]
    out["description"] = value["description"]
    out["recommendation"] = value["recommendation"]
    import aws_sdk_inspector.types.scope_list

    out["scopes"] = aws_sdk_inspector.types.scope_list.serialize_aws_json_1_1(
        value["scopes"]
    )
    if "attributes" in value:
        import aws_sdk_inspector.types.attribute_list

        out["attributes"] = (
            aws_sdk_inspector.types.attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Exclusion:
    out: Exclusion = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Exclusion.arn required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("Exclusion.title required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("Exclusion.description required")
    if "recommendation" in data:
        out["recommendation"] = data["recommendation"]
    else:
        raise DeserializationError("Exclusion.recommendation required")
    if "scopes" in data:
        import aws_sdk_inspector.types.scope_list

        out["scopes"] = aws_sdk_inspector.types.scope_list.deserialize_aws_json_1_1(
            data["scopes"]
        )
    else:
        raise DeserializationError("Exclusion.scopes required")
    if "attributes" in data:
        import aws_sdk_inspector.types.attribute_list

        out["attributes"] = (
            aws_sdk_inspector.types.attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.inspector#ExclusionPreview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.attribute_list
    import capo_inspector.types.scope_list
    import capo_inspector.types.text


class ExclusionPreview(TypedDict, closed=True):
    title: "capo_inspector.types.text.Text"
    """<p>The name of the exclusion preview.</p>"""
    description: "capo_inspector.types.text.Text"
    """<p>The description of the exclusion preview.</p>"""
    recommendation: "capo_inspector.types.text.Text"
    """<p>The recommendation for the exclusion preview.</p>"""
    scopes: "capo_inspector.types.scope_list.ScopeList"
    """<p>The AWS resources for which the exclusion preview pertains.</p>"""
    attributes: NotRequired["capo_inspector.types.attribute_list.AttributeList"]
    """<p>The system-defined attributes for the exclusion preview.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExclusionPreview) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["description"] = value["description"]
    out["recommendation"] = value["recommendation"]
    import capo_inspector.types.scope_list

    out["scopes"] = capo_inspector.types.scope_list.serialize_aws_json_1_1(
        value["scopes"]
    )
    if "attributes" in value:
        import capo_inspector.types.attribute_list

        out["attributes"] = capo_inspector.types.attribute_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExclusionPreview:
    out: ExclusionPreview = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ExclusionPreview.title required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("ExclusionPreview.description required")
    if "recommendation" in data:
        out["recommendation"] = data["recommendation"]
    else:
        raise DeserializationError("ExclusionPreview.recommendation required")
    if "scopes" in data:
        import capo_inspector.types.scope_list

        out["scopes"] = capo_inspector.types.scope_list.deserialize_aws_json_1_1(
            data["scopes"]
        )
    else:
        raise DeserializationError("ExclusionPreview.scopes required")
    if "attributes" in data:
        import capo_inspector.types.attribute_list

        out["attributes"] = (
            capo_inspector.types.attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    return out

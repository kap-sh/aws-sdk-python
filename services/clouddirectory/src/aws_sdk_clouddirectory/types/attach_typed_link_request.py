"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachTypedLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.attribute_name_and_value_list
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name


class AttachTypedLinkRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.</p>"""
    source_object_reference: (
        "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    )
    """<p>Identifies the source object that the typed link will attach to.</p>"""
    target_object_reference: (
        "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    )
    """<p>Identifies the target object that the typed link will attach to.</p>"""
    typed_link_facet: "aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.TypedLinkSchemaAndFacetName"
    """<p>Identifies the typed link facet that is associated with the typed link.</p>"""
    attributes: "aws_sdk_clouddirectory.types.attribute_name_and_value_list.AttributeNameAndValueList"
    """<p>A set of attributes that are associated with the typed link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachTypedLinkRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["SourceObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["source_object_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.object_reference

    out["TargetObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["target_object_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name

    out["TypedLinkFacet"] = (
        aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.serialize_json(
            value["typed_link_facet"]
        )
    )
    import aws_sdk_clouddirectory.types.attribute_name_and_value_list

    out["Attributes"] = (
        aws_sdk_clouddirectory.types.attribute_name_and_value_list.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> AttachTypedLinkRequest:
    out: AttachTypedLinkRequest = {}  # type: ignore[typeddict-item]
    if "SourceObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["source_object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["SourceObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "AttachTypedLinkRequest.source_object_reference required"
        )
    if "TargetObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["target_object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["TargetObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "AttachTypedLinkRequest.target_object_reference required"
        )
    if "TypedLinkFacet" in data:
        import aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name

        out["typed_link_facet"] = (
            aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.deserialize_json(
                data["TypedLinkFacet"]
            )
        )
    else:
        raise DeserializationError("AttachTypedLinkRequest.typed_link_facet required")
    if "Attributes" in data:
        import aws_sdk_clouddirectory.types.attribute_name_and_value_list

        out["attributes"] = (
            aws_sdk_clouddirectory.types.attribute_name_and_value_list.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("AttachTypedLinkRequest.attributes required")
    return out

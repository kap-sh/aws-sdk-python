"""Generated from Smithy shape ``com.amazonaws.s3control#S3Grantee``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.non_empty_max_length1024_string
    import capo_s3_control.types.s3_grantee_type_identifier


class S3Grantee(TypedDict, closed=True):
    type_identifier: NotRequired[
        "capo_s3_control.types.s3_grantee_type_identifier.S3GranteeTypeIdentifier"
    ]
    """<p></p>"""
    identifier: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    display_name: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Grantee, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "type_identifier" in value:
        import capo_s3_control.types.s3_grantee_type_identifier

        capo_s3_control.types.s3_grantee_type_identifier.serialize_xml(
            value["type_identifier"], el, "TypeIdentifier"
        )
    if "identifier" in value:
        SubElement(el, "Identifier").text = str(value["identifier"])
    if "display_name" in value:
        SubElement(el, "DisplayName").text = str(value["display_name"])


def deserialize_xml(el: Element) -> S3Grantee:
    out: S3Grantee = {}  # type: ignore[typeddict-item]
    child_type_identifier = el.find("TypeIdentifier")
    if child_type_identifier is not None:
        import capo_s3_control.types.s3_grantee_type_identifier

        out["type_identifier"] = (
            capo_s3_control.types.s3_grantee_type_identifier.deserialize_xml(
                child_type_identifier
            )
        )
    child_identifier = el.find("Identifier")
    if child_identifier is not None:
        out["identifier"] = str(child_identifier.text or "")
    child_display_name = el.find("DisplayName")
    if child_display_name is not None:
        out["display_name"] = str(child_display_name.text or "")
    return out

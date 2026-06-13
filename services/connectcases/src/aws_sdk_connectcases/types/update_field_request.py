"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateFieldRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.field_attributes
    import aws_sdk_connectcases.types.field_description
    import aws_sdk_connectcases.types.field_id
    import aws_sdk_connectcases.types.field_name


class UpdateFieldRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    field_id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>The unique identifier of a field.</p>"""
    name: NotRequired["aws_sdk_connectcases.types.field_name.FieldName"]
    """<p>The name of the field.</p>"""
    description: NotRequired[
        "aws_sdk_connectcases.types.field_description.FieldDescription"
    ]
    """<p>The description of a field.</p>"""
    attributes: NotRequired[
        "aws_sdk_connectcases.types.field_attributes.FieldAttributes"
    ]
    """<p>Union of field attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFieldRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "attributes" in value:
        import aws_sdk_connectcases.types.field_attributes

        out["attributes"] = aws_sdk_connectcases.types.field_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFieldRequest:
    out: UpdateFieldRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "attributes" in data:
        import aws_sdk_connectcases.types.field_attributes

        out["attributes"] = (
            aws_sdk_connectcases.types.field_attributes.deserialize_json(
                data["attributes"]
            )
        )
    return out

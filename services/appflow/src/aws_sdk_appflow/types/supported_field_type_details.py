"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedFieldTypeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.field_type_details


class SupportedFieldTypeDetails(TypedDict, closed=True):
    v1: "aws_sdk_appflow.types.field_type_details.FieldTypeDetails"
    """<p> The initial supported version for <code>fieldType</code>. If this is later changed to a different version, v2 will be introduced. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportedFieldTypeDetails) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.field_type_details

    out["v1"] = aws_sdk_appflow.types.field_type_details.serialize_json(value["v1"])
    return out


def deserialize_json(data: dict) -> SupportedFieldTypeDetails:
    out: SupportedFieldTypeDetails = {}  # type: ignore[typeddict-item]
    if "v1" in data:
        import aws_sdk_appflow.types.field_type_details

        out["v1"] = aws_sdk_appflow.types.field_type_details.deserialize_json(
            data["v1"]
        )
    else:
        raise DeserializationError("SupportedFieldTypeDetails.v1 required")
    return out

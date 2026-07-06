"""Generated from Smithy shape ``com.amazonaws.glacier#Grantee``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glacier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string
    import aws_sdk_glacier.types.type


class Grantee(TypedDict, closed=True):
    type: "aws_sdk_glacier.types.type.Type"
    """<p>Type of grantee</p>"""
    display_name: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Screen name of the grantee.</p>"""
    uri: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>URI of the grantee group.</p>"""
    id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The canonical user ID of the grantee.</p>"""
    email_address: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Email address of the grantee.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Grantee) -> dict:
    out: dict = {}
    import aws_sdk_glacier.types.type

    out["Type"] = aws_sdk_glacier.types.type.serialize_json(value["type"])
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "uri" in value:
        out["URI"] = value["uri"]
    if "id" in value:
        out["ID"] = value["id"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> Grantee:
    out: Grantee = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_glacier.types.type

        out["type"] = aws_sdk_glacier.types.type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("Grantee.type required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "URI" in data:
        out["uri"] = data["URI"]
    if "ID" in data:
        out["id"] = data["ID"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    return out

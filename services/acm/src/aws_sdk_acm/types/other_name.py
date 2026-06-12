"""Generated from Smithy shape ``com.amazonaws.acm#OtherName``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.string


class OtherName(TypedDict):
    object_identifier: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>Specifies an OID.</p>"""
    value: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>Specifies an OID value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OtherName) -> dict:
    out: dict = {}
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OtherName:
    out: OtherName = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out

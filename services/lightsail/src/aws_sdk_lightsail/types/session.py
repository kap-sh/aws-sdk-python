"""Generated from Smithy shape ``com.amazonaws.lightsail#Session``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.sensitive_non_empty_string


class Session(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The session name.</p>"""
    url: NotRequired[
        "aws_sdk_lightsail.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The session URL.</p>"""
    is_primary: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>When true, this Boolean value indicates the primary session for the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "url" in value:
        out["url"] = value["url"]
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "url" in data:
        out["url"] = data["url"]
    if "isPrimary" in data:
        out["is_primary"] = data["isPrimary"]
    return out

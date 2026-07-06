"""Generated from Smithy shape ``com.amazonaws.eventbridge#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.string


class Condition(TypedDict, closed=True):
    type: "aws_sdk_eventbridge.types.string.String"
    """<p>Specifies the type of condition. Currently the only supported value is <code>StringEquals</code>.</p>"""
    key: "aws_sdk_eventbridge.types.string.String"
    """<p>Specifies the key for the condition. Currently the only supported key is <code>aws:PrincipalOrgID</code>.</p>"""
    value: "aws_sdk_eventbridge.types.string.String"
    """<p>Specifies the value for the key. Currently, this must be the ID of the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Condition) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("Condition.type required")
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Condition.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Condition.value required")
    return out

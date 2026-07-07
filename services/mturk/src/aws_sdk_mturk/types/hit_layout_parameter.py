"""Generated from Smithy shape ``com.amazonaws.mturk#HITLayoutParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.string


class HITLayoutParameter(TypedDict, closed=True):
    name: "aws_sdk_mturk.types.string.String"
    """<p> The name of the parameter in the HITLayout. </p>"""
    value: "aws_sdk_mturk.types.string.String"
    """<p>The value substituted for the parameter referenced in the HITLayout. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITLayoutParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HITLayoutParameter:
    out: HITLayoutParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("HITLayoutParameter.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("HITLayoutParameter.value required")
    return out

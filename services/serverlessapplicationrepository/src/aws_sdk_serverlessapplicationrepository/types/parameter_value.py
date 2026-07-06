"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ParameterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class ParameterValue(TypedDict, closed=True):
    name: NotRequired["aws_sdk_serverlessapplicationrepository.types.__string.__string"]
    """<p>The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.</p>"""
    value: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The input value associated with the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterValue) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ParameterValue:
    out: ParameterValue = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out

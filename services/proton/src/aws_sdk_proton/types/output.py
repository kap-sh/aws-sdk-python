"""Generated from Smithy shape ``com.amazonaws.proton#Output``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.output_key
    import aws_sdk_proton.types.output_value_string


class Output(TypedDict):
    key: NotRequired["aws_sdk_proton.types.output_key.OutputKey"]
    """<p>The output key.</p>"""
    value_string: NotRequired[
        "aws_sdk_proton.types.output_value_string.OutputValueString"
    ]
    """<p>The output value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Output) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value_string" in value:
        out["valueString"] = value["value_string"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Output:
    out: Output = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "valueString" in data:
        out["value_string"] = data["valueString"]
    return out

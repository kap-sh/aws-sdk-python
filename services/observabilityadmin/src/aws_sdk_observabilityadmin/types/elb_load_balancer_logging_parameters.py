"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ELBLoadBalancerLoggingParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.output_format


class ELBLoadBalancerLoggingParameters(TypedDict, closed=True):
    output_format: NotRequired[
        "aws_sdk_observabilityadmin.types.output_format.OutputFormat"
    ]
    """<p> The format for ELB access log entries (plain text or JSON format). </p>"""
    field_delimiter: NotRequired["str"]
    """<p> The delimiter character used to separate fields in ELB access log entries when using plain text format. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ELBLoadBalancerLoggingParameters) -> dict:
    out: dict = {}
    if "output_format" in value:
        import aws_sdk_observabilityadmin.types.output_format

        out["OutputFormat"] = (
            aws_sdk_observabilityadmin.types.output_format.serialize_json(
                value["output_format"]
            )
        )
    if "field_delimiter" in value:
        out["FieldDelimiter"] = value["field_delimiter"]
    return out


def deserialize_json(data: dict) -> ELBLoadBalancerLoggingParameters:
    out: ELBLoadBalancerLoggingParameters = {}  # type: ignore[typeddict-item]
    if "OutputFormat" in data:
        import aws_sdk_observabilityadmin.types.output_format

        out["output_format"] = (
            aws_sdk_observabilityadmin.types.output_format.deserialize_json(
                data["OutputFormat"]
            )
        )
    if "FieldDelimiter" in data:
        out["field_delimiter"] = data["FieldDelimiter"]
    return out

"""Generated from Smithy shape ``com.amazonaws.b2bi#X12OutboundEdiHeaders``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.x12_control_numbers
    import capo_b2bi.types.x12_delimiters
    import capo_b2bi.types.x12_functional_group_headers
    import capo_b2bi.types.x12_gs05_time_format
    import capo_b2bi.types.x12_interchange_control_headers
    import capo_b2bi.types.x12_validate_edi


class X12OutboundEdiHeaders(TypedDict, closed=True):
    interchange_control_headers: NotRequired[
        "capo_b2bi.types.x12_interchange_control_headers.X12InterchangeControlHeaders"
    ]
    """<p>In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header.</p>"""
    functional_group_headers: NotRequired[
        "capo_b2bi.types.x12_functional_group_headers.X12FunctionalGroupHeaders"
    ]
    """<p>The functional group headers for the X12 object.</p>"""
    delimiters: NotRequired["capo_b2bi.types.x12_delimiters.X12Delimiters"]
    """<p>The delimiters, for example semicolon (<code>;</code>), that separates sections of the headers for the X12 object.</p>"""
    validate_edi: NotRequired["capo_b2bi.types.x12_validate_edi.X12ValidateEdi"]
    """<p>Specifies whether or not to validate the EDI for this X12 object: <code>TRUE</code> or <code>FALSE</code>. When enabled, this performs both standard EDI validation and applies any configured custom validation rules including element length constraints, code list validations, and element requirement checks. Validation results are returned in the response validation messages.</p>"""
    control_numbers: NotRequired[
        "capo_b2bi.types.x12_control_numbers.X12ControlNumbers"
    ]
    """<p>Specifies control number configuration for outbound X12 EDI headers. These settings determine the starting values for interchange, functional group, and transaction set control numbers.</p>"""
    gs05_time_format: NotRequired[
        "capo_b2bi.types.x12_gs05_time_format.X12GS05TimeFormat"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12OutboundEdiHeaders) -> dict:
    out: dict = {}
    if "interchange_control_headers" in value:
        import capo_b2bi.types.x12_interchange_control_headers

        out["interchangeControlHeaders"] = (
            capo_b2bi.types.x12_interchange_control_headers.serialize_aws_json_1_0(
                value["interchange_control_headers"]
            )
        )
    if "functional_group_headers" in value:
        import capo_b2bi.types.x12_functional_group_headers

        out["functionalGroupHeaders"] = (
            capo_b2bi.types.x12_functional_group_headers.serialize_aws_json_1_0(
                value["functional_group_headers"]
            )
        )
    if "delimiters" in value:
        import capo_b2bi.types.x12_delimiters

        out["delimiters"] = capo_b2bi.types.x12_delimiters.serialize_aws_json_1_0(
            value["delimiters"]
        )
    if "validate_edi" in value:
        out["validateEdi"] = value["validate_edi"]
    if "control_numbers" in value:
        import capo_b2bi.types.x12_control_numbers

        out["controlNumbers"] = (
            capo_b2bi.types.x12_control_numbers.serialize_aws_json_1_0(
                value["control_numbers"]
            )
        )
    if "gs05_time_format" in value:
        import capo_b2bi.types.x12_gs05_time_format

        out["gs05TimeFormat"] = (
            capo_b2bi.types.x12_gs05_time_format.serialize_aws_json_1_0(
                value["gs05_time_format"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12OutboundEdiHeaders:
    out: X12OutboundEdiHeaders = {}  # type: ignore[typeddict-item]
    if "interchangeControlHeaders" in data:
        import capo_b2bi.types.x12_interchange_control_headers

        out["interchange_control_headers"] = (
            capo_b2bi.types.x12_interchange_control_headers.deserialize_aws_json_1_0(
                data["interchangeControlHeaders"]
            )
        )
    if "functionalGroupHeaders" in data:
        import capo_b2bi.types.x12_functional_group_headers

        out["functional_group_headers"] = (
            capo_b2bi.types.x12_functional_group_headers.deserialize_aws_json_1_0(
                data["functionalGroupHeaders"]
            )
        )
    if "delimiters" in data:
        import capo_b2bi.types.x12_delimiters

        out["delimiters"] = capo_b2bi.types.x12_delimiters.deserialize_aws_json_1_0(
            data["delimiters"]
        )
    if "validateEdi" in data:
        out["validate_edi"] = data["validateEdi"]
    if "controlNumbers" in data:
        import capo_b2bi.types.x12_control_numbers

        out["control_numbers"] = (
            capo_b2bi.types.x12_control_numbers.deserialize_aws_json_1_0(
                data["controlNumbers"]
            )
        )
    if "gs05TimeFormat" in data:
        import capo_b2bi.types.x12_gs05_time_format

        out["gs05_time_format"] = (
            capo_b2bi.types.x12_gs05_time_format.deserialize_aws_json_1_0(
                data["gs05TimeFormat"]
            )
        )
    return out

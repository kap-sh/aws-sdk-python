"""Generated from Smithy shape ``com.amazonaws.b2bi#AdvancedOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_advanced_options


class AdvancedOptions(TypedDict, closed=True):
    x12: NotRequired["aws_sdk_b2bi.types.x12_advanced_options.X12AdvancedOptions"]
    """<p>A structure that contains X12-specific advanced options, such as split options for processing X12 EDI files.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdvancedOptions) -> dict:
    out: dict = {}
    if "x12" in value:
        import aws_sdk_b2bi.types.x12_advanced_options

        out["x12"] = aws_sdk_b2bi.types.x12_advanced_options.serialize_aws_json_1_0(
            value["x12"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AdvancedOptions:
    out: AdvancedOptions = {}  # type: ignore[typeddict-item]
    if "x12" in data:
        import aws_sdk_b2bi.types.x12_advanced_options

        out["x12"] = aws_sdk_b2bi.types.x12_advanced_options.deserialize_aws_json_1_0(
            data["x12"]
        )
    return out

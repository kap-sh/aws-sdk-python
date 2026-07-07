"""Generated from Smithy shape ``com.amazonaws.b2bi#X12AdvancedOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_split_options
    import aws_sdk_b2bi.types.x12_validation_options


class X12AdvancedOptions(TypedDict, closed=True):
    split_options: NotRequired["aws_sdk_b2bi.types.x12_split_options.X12SplitOptions"]
    """<p>Specifies options for splitting X12 EDI files. These options control how large X12 files are divided into smaller, more manageable units.</p>"""
    validation_options: NotRequired[
        "aws_sdk_b2bi.types.x12_validation_options.X12ValidationOptions"
    ]
    """<p>Specifies validation options for X12 EDI processing. These options control how validation rules are applied during EDI document processing, including custom validation rules for element length constraints, code list validations, and element requirement checks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12AdvancedOptions) -> dict:
    out: dict = {}
    if "split_options" in value:
        import aws_sdk_b2bi.types.x12_split_options

        out["splitOptions"] = (
            aws_sdk_b2bi.types.x12_split_options.serialize_aws_json_1_0(
                value["split_options"]
            )
        )
    if "validation_options" in value:
        import aws_sdk_b2bi.types.x12_validation_options

        out["validationOptions"] = (
            aws_sdk_b2bi.types.x12_validation_options.serialize_aws_json_1_0(
                value["validation_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12AdvancedOptions:
    out: X12AdvancedOptions = {}  # type: ignore[typeddict-item]
    if "splitOptions" in data:
        import aws_sdk_b2bi.types.x12_split_options

        out["split_options"] = (
            aws_sdk_b2bi.types.x12_split_options.deserialize_aws_json_1_0(
                data["splitOptions"]
            )
        )
    if "validationOptions" in data:
        import aws_sdk_b2bi.types.x12_validation_options

        out["validation_options"] = (
            aws_sdk_b2bi.types.x12_validation_options.deserialize_aws_json_1_0(
                data["validationOptions"]
            )
        )
    return out

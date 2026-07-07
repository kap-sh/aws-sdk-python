"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ValidationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_validation_rules


class X12ValidationOptions(TypedDict, closed=True):
    validation_rules: NotRequired[
        "aws_sdk_b2bi.types.x12_validation_rules.X12ValidationRules"
    ]
    """<p>Specifies a list of validation rules to apply during EDI document processing. These rules can include code list modifications, element length constraints, and element requirement changes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ValidationOptions) -> dict:
    out: dict = {}
    if "validation_rules" in value:
        import aws_sdk_b2bi.types.x12_validation_rules

        out["validationRules"] = (
            aws_sdk_b2bi.types.x12_validation_rules.serialize_aws_json_1_0(
                value["validation_rules"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12ValidationOptions:
    out: X12ValidationOptions = {}  # type: ignore[typeddict-item]
    if "validationRules" in data:
        import aws_sdk_b2bi.types.x12_validation_rules

        out["validation_rules"] = (
            aws_sdk_b2bi.types.x12_validation_rules.deserialize_aws_json_1_0(
                data["validationRules"]
            )
        )
    return out

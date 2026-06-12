"""Generated from Smithy shape ``com.amazonaws.glue#DecimalNumber``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.blob
    import aws_sdk_glue.types.integer


class DecimalNumber(TypedDict):
    unscaled_value: "aws_sdk_glue.types.blob.Blob"
    """<p>The unscaled numeric value.</p>"""
    scale: "aws_sdk_glue.types.integer.Integer"
    """<p>The scale that determines where the decimal point falls in the unscaled value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecimalNumber) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.blob

    out["UnscaledValue"] = aws_sdk_glue.types.blob.serialize_aws_json_1_1(
        value["unscaled_value"]
    )
    out["Scale"] = value.get("scale", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DecimalNumber:
    out: DecimalNumber = {}  # type: ignore[typeddict-item]
    if "UnscaledValue" in data:
        import aws_sdk_glue.types.blob

        out["unscaled_value"] = aws_sdk_glue.types.blob.deserialize_aws_json_1_1(
            data["UnscaledValue"]
        )
    else:
        raise DeserializationError("DecimalNumber.unscaled_value required")
    if "Scale" in data:
        out["scale"] = data["Scale"]
    else:
        out["scale"] = 0
    return out

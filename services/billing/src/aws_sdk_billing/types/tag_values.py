"""Generated from Smithy shape ``com.amazonaws.billing#TagValues``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.tag_key
    import aws_sdk_billing.types.values


class TagValues(TypedDict):
    key: "aws_sdk_billing.types.tag_key.TagKey"
    """<p> The key for the tag. </p>"""
    values: "aws_sdk_billing.types.values.Values"
    """<p> The specific value of the tag. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagValues) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_billing.types.values

    out["values"] = aws_sdk_billing.types.values.serialize_aws_json_1_0(value["values"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagValues:
    out: TagValues = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("TagValues.key required")
    if "values" in data:
        import aws_sdk_billing.types.values

        out["values"] = aws_sdk_billing.types.values.deserialize_aws_json_1_0(
            data["values"]
        )
    else:
        raise DeserializationError("TagValues.values required")
    return out

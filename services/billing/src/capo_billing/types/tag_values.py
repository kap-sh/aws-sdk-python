"""Generated from Smithy shape ``com.amazonaws.billing#TagValues``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.tag_key
    import capo_billing.types.values


class TagValues(TypedDict, closed=True):
    key: "capo_billing.types.tag_key.TagKey"
    """<p> The key for the tag. </p>"""
    values: "capo_billing.types.values.Values"
    """<p> The specific value of the tag. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagValues) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_billing.types.values

    out["values"] = capo_billing.types.values.serialize_aws_json_1_0(value["values"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagValues:
    out: TagValues = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("TagValues.key required")
    if "values" in data:
        import capo_billing.types.values

        out["values"] = capo_billing.types.values.deserialize_aws_json_1_0(
            data["values"]
        )
    else:
        raise DeserializationError("TagValues.values required")
    return out

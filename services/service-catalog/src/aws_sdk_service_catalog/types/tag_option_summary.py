"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_key
    import aws_sdk_service_catalog.types.tag_option_values


class TagOptionSummary(TypedDict, closed=True):
    key: NotRequired["aws_sdk_service_catalog.types.tag_option_key.TagOptionKey"]
    """<p>The TagOption key.</p>"""
    values: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_values.TagOptionValues"
    ]
    """<p>The TagOption value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionSummary) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import aws_sdk_service_catalog.types.tag_option_values

        out["Values"] = (
            aws_sdk_service_catalog.types.tag_option_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagOptionSummary:
    out: TagOptionSummary = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import aws_sdk_service_catalog.types.tag_option_values

        out["values"] = (
            aws_sdk_service_catalog.types.tag_option_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
